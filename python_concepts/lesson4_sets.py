s = set()
print(type(s))

s.add(1)
s.add(2)
s.union({1, 2, 3})
print(s)
s1 = s.union({1, 2, 3})
print(s, s1)
s2 = s.intersection({1, 2, 3})
print(s, s2)

s_from_list = set([1, 2, 3, 4])
print(type(s_from_list))

l = set([1, 2, 3, 4])
s_from_lists = set(l)
print(type(s_from_lists))
""" OR """
alpha_sets = {'A', 'B', 'C', 'D'}
print(type(alpha_sets))