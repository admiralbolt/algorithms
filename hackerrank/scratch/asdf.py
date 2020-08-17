"""
WITHOUT CACHING
================
trie init time: 0.010449647903442383
parse words time: 3.3627960681915283
suffix links time: 3.4872419834136963
output links time: 2.2487218379974365
get_occurences time: 2.0044186115264893
total: 11.10338020324707

MANUAL CACHING
==============
trie init time: 0.012773990631103516
parse words time: 3.549691677093506
suffix links time: 3.2703161239624023
output links time: 2.2342305183410645
get_occurences time: 1.9397037029266357
total: 10.99414849281311

FASTER 07
=======
trie init time: 2.288818359375e-05
parse keywords time: 7.685137748718262
suffix links time: 9.423442602157593
total construction: 17.10877275466919

trie init time: 2.002716064453125e-05
parse keywords time: 7.55479884147644
suffix links time: 9.511631727218628
total construction: 17.066583156585693

SLOWER 07
==========
trie init time: 2.1457672119140625e-05
parse keywords time: 7.970995903015137
suffix links time: 9.22016167640686
total construction: 17.191315412521362


"""

"""
a, ab, abc, abcd
sort(length, alphabet) -> ???

abcd, aba, abc

# process abcd
a -> b -> c -> d
# process aba
# check if aba exists mark it as output node
# check if ab exists process letters after existing prefix.


"""
