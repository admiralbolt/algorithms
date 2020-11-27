import timeit
import textwrap

def time_triplet_chain():
  setup = textwrap.dedent("""
  import decreasing_triplet
  import random

  random.seed("slartibartfast")
  l = [random.randint(0, 1000) for i in range(1000)]
  """)
  t = timeit.Timer("decreasing_triplet.decreasing_triplet_chain(l)", setup=setup).repeat(5, 100)
  print(t)
  print(min(t))

def time_triplet():
  setup = textwrap.dedent("""
  import decreasing_triplet
  import random

  random.seed("slartibartfast")
  l = [random.randint(0, 1000) for i in range(1000)]
  """)
  t = timeit.Timer("decreasing_triplet.decreasing_triplet(l)", setup=setup).repeat(5, 100)
  print(t)
  print(min(t))

time_triplet_chain()
time_triplet()
