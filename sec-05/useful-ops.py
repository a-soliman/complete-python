print('=' * 10, '| zipping |', '=' * 10)

# zipping
l1 = [1,2,3,4]
l2 = ['a', 'b', 'c', 'd']

for item in zip(l1,l2):
    print(item)

print('=' * 10, '| enumerate |', '=' * 10)

# enumerate
word = 'hello world'

for index, letter in enumerate(word):
    print(index, letter)


print('=' * 10, '| IN |', '=' * 10)

#in 
print(3 in [2,3,5,4])

print('=' * 10, '| min |', '=' * 10)

# min
print(min([20,5,50,4]))


print('=' * 10, '| max |', '=' * 10)

# max
print(max([20,5,50,4]))