"""
A class for represnting and building nfas.
"""
import collections

from graphviz import Digraph
from pprint import pprint

class Node:
  """It's a node!

  In this case we only need to track a number just to identify the node.
  """

  def __init__(self, number):
    self.number = number

  def __hash__(self):
    return self.number

  def __repr__(self):
    return f"N({self.number})"

class Ticker:
  """An unnecessary helper class that maintains state to get sequential numbers."""

  def __init__(self):
    self.number = -1

  def next(self):
    self.number += 1
    return self.number


class Edge:
  """It's an edge!

  Special handling is done for epsilon values.
  """

  def __init__(self, source, sink, value):
    self.source = source
    self.sink = sink
    # Epsilon transitions are tracked by the literal string "epsilon".
    self.value = "ε" if value == "epsilon" else value
    return

  def is_epsilon(self):
    return self.value == "ε"

  def __repr__(self):
    return f"({self.source}, {self.sink}, {self.value})"

  def __hash__(self):
    return hash((self.source, self.sink))

class NFA:
  """A class representing a non-deterministic finite state automaton.

  Tracks edges from both incoming and outgoing directions.
  Can be mutated directly via helper methods:
    add_node()
    add_edge()
    remove_edge()
  or combined with other automaton:
    nfa_or()
    nfa_and()
    star()
  """

  def __init__(self, ticker):
    self.ticker = ticker
    self.start = Node(self.ticker.next())
    self.end = Node(self.ticker.next())
    self.nodes = set([self.start, self.end])
    self.outgoing_edges = collections.defaultdict(set)
    self.incoming_edges = collections.defaultdict(set)

  def render(self, fname):
    """Renders the automaton to a graph using graphviz."""
    d = Digraph()
    d.graph_attr["rankdir"] = "LR"
    for node in self.nodes:
      d.node(str(node.number), str(node.number))

    for source, edges in self.outgoing_edges.items():
      for edge in edges:
        d.edge(str(edge.source.number), str(edge.sink.number), label=edge.value)

    d.render(fname)


  def add_node(self):
    """Adds and returns a new node."""
    n = Node(self.ticker.next())
    self.nodes.add(n)
    return n


  def add_edge(self, source, sink, value):
    """Adds an edge, tracking by both incoming and outgoing."""
    e = Edge(source, sink, value)
    self.outgoing_edges[source].add(e)
    self.incoming_edges[sink].add(e)
    return e


  def remove_edge(self, edge):
    """Deletes an edge from both outgoing & incoming."""
    self.outgoing_edges[edge.source].remove(edge)
    self.incoming_edges[edge.sink].remove(edge)


  def from_a(self, a):
    """Creates a simple NFA from a single value."""
    self.add_edge(self.start, self.end, a)


  def merge(self, nfa):
    """Merges in all nodes and edges from another automaton."""
    self.nodes.update(nfa.nodes)
    for sink, edges in nfa.incoming_edges.items():
      self.incoming_edges[sink].update(edges)

    for source, edges in nfa.outgoing_edges.items():
      self.outgoing_edges[source].update(edges)


  def merge_node(self, n1, n2):
    """Merges two nodes.

    This shifts all the edges going into and out of n2.
    All outgoing edges (n2 -> somenode) are updated to (n1 -> somenode)
    All incoming edges (somenode -> n2) are updated to (somenode -> n1)
    """
    edges = self.outgoing_edges[n2].copy()
    for edge in edges:
      self.remove_edge(edge)
      self.add_edge(n1, edge.sink, edge.value)

    edges = self.incoming_edges[n2].copy()
    for edge in edges:
      self.remove_edge(edge)
      self.add_edge(edge.source, n1, edge.value)

    self.nodes.remove(n2)


  def nfa_or(self, nfa):
    """Updates the current NFA to be a logical or of itself and the passed in nfa."""
    self.merge(nfa)
    self.merge_node(self.start, nfa.start)
    self.merge_node(self.end, nfa.end)


  def nfa_and(self, nfa):
    """Updates the current NFA to be directly followed by the passed in nfa."""
    self.merge(nfa)
    self.merge_node(self.end, nfa.start)
    self.end = nfa.end


  def star(self):
    """Allow the current NFA to match anynumber of times."""
    self.add_edge(self.end, self.start, "epsilon")
    new_start = self.add_node()
    new_end = self.add_node()
    self.add_edge(new_start, new_end, "epsilon")
    self.add_edge(new_start, self.start, "epsilon")
    self.add_edge(self.end, new_end, "epsilon")
    self.start = new_start
    self.end = new_end



if __name__ == "__main__":
  ticker = Ticker()
  a = NFA(ticker)
  a.from_a("a")

  b = NFA(ticker)
  b.from_a("b")

  a.nfa_and(b)
  a.render("ab.gv")

  s = NFA(ticker)
  s.from_a("a")
  s.render("a.gv")
  s.star()
  s.render("star.gv")

  a.nfa_or(s)
  a.render("or.gv")

  a.star()
  a.render("orstar.gv")
