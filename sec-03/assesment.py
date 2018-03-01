# reverse 'hello'
reverse = 'hello'[::-1]
print(reverse)

# grap the last letter of 'hello' using two methods
one = 'hello'[-1::]
print(one)
two = 'hello'[len('hello')-1::]
print(two)

# Build a list [0,0,0] in two separate ways

l1 = list([0,0,0])
l2 = list()
l2.append(0)
l2 = l2 + [0,0]

print('List one: ', l1)
print('List otwo: ', l2)

#change 'hello' to say 'goodbye' in the following
list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'
print(list3)


# sort the following list
list4 = [5,3,4,6,1]
list4.sort()
print(list4)


# grap the word 'hello' of all the following dictionaries

d1 = {'key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

print(d1['key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])


#use a set to find the unique values of the list below
new_list = [1,2,2,33,4,4,11,22,3,3,2]
new_set = set(new_list)
print(new_set)