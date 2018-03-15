l = [1,2,3]

l.append(4)
l = l + [1]

print(l)

print(l.count(1))

x = l.copy()
x.append([5,6,7])

x.extend([8,9,10])

print(x)
print(x.index(10))

x.insert(0, 'Inserted')
print(x)

