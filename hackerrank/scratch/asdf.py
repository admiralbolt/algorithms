"""
INPUT07
=======

WITHOUT CACHING
---------------
warmup: 0.16127872467041016
trie2 init time: 8.988380432128906e-05
total construction time: 10.79426121711731
0 7353994
GRAND TOTAL: 11.12623643875122

INPUT33
=======

warmup: 0.15894031524658203
trie2 init time: 6.532669067382812e-05
total construction time: 5.41740870475769
0 7353994
GRAND TOTAL: 5.730339288711548

warmup: 0.14467263221740723
trie2 init time: 5.7220458984375e-05
total construction time: 5.130284309387207
0 7353994
GRAND TOTAL: 5.47948431968689   






PROFILE#1
trie2 init time: 6.365776062011719e-05
         16851630 function calls in 35.335 seconds

   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001   35.335   35.335 <string>:1(<module>)
  1261350    3.649    0.000    3.649    0.000 aho_corasick.py:133(__init__)
  2238127    1.659    0.000    1.659    0.000 aho_corasick.py:148(__eq__)
  1261350    4.336    0.000    7.810    0.000 aho_corasick.py:151(__hash__)
  1261350    1.848    0.000   11.508    0.000 aho_corasick.py:154(add_child)
  1261350    2.063    0.000   13.571    0.000 aho_corasick.py:22(add_node)
  1261345    5.132    0.000    5.832    0.000 aho_corasick.py:28(get_longest_strict_suffix)
        1    8.704    8.704   35.334   35.334 aho_corasick.py:43(construct)
        1    0.073    0.073    0.142    0.142 aho_corasick.py:45(<listcomp>)
  1261350    1.144    0.000    1.144    0.000 {built-in method _hashlib.openssl_sha1}
        1    0.000    0.000   35.335   35.335 {built-in method builtins.exec}
  2000000    1.334    0.000    1.334    0.000 {built-in method builtins.len}
        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
        1    0.023    0.023    0.023    0.023 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 {built-in method time.time}
  1261350    1.850    0.000    9.660    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1261350    1.031    0.000    1.031    0.000 {method 'encode' of 'str' objects}
  1261350    1.189    0.000    1.189    0.000 {method 'get' of 'dict' objects}
  1261350    1.299    0.000    1.299    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}
"""
