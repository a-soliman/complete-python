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

vowels = 'aioue'
sent = 'Hey there my name is ahmed'

l4 = [ x.upper() for x in sent if x in vowels ]

print(l4)

c = [32, 0, -10, 50]
f = [ ( (9/5)*temp + 32) for temp in c]
print(f)

f2 = []

for temp in c:
      f2.append( (9/5)* temp + 32)

print(f2)

