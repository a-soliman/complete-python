my_string = 'hello'
my_list = []

for letter in my_string:
      my_list.append(letter)

print(my_list)

new_list = [ x for x in my_string]

print(new_list)

l2 = [ letter for letter in 'Hey, How is it goint']

print(l2)

l3 = [ num + 2 for num in range(0, 11) if num %2 == 0]
print(l3)



