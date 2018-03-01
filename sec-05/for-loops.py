my_list = [1,2,3,2,1,3,5,6]

for num in my_list:
    if num % 2 == 0:
        print(num)


print('=' * 20 )
# Tuple unpacking
new_list = [(1,2), (3,4), (5,6), (7,8)]

for (a,b) in new_list:
    print(a)
    print(b)
    print('-')


print('=' * 20 )
# Tuple unpacking in dictionaries

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(key)