s = set()

s.add(1)
s.add(2)
s.add(2)

print(s)

s.clear()
print(s)

s = {1,2,3}
s2 = s.copy()
print(s2)

s.add('Original')
print(s)
print(s2)


print(s.difference(s2))