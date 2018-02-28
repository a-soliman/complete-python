
my_list = [1, 'two', 3, True]

print(len(my_list))

two = my_list[1]
print(two)

# concatinating
print(my_list + ['hello there'])

# Appending
my_list.append(55)
my_list[0] = 'One'
print(my_list)


# POP
poped_item = my_list.pop(0)

print(poped_item)


# SORT

new_list = ['e', 'h', 'c', 'z', 'a']

num_list = [4, 1, 5,20, 8, 2]

print(new_list)
new_list.sort()
print(new_list)

print(num_list)
num_list.sort()
print(num_list)

# REVERSE
num_list.reverse()
print(num_list)

new_list.reverse()
print(new_list)

