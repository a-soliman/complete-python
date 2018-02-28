my_dict = { 'key1': 'value1', 'key2': 'value2'}

print(my_dict['key1'])

prices = { 'banana': 3.00, 'apple': 1.99, 'orange': 5.20 }

print(prices['apple'])

# ADDING
prices['milk'] = 2.99
print(prices)

# DELETING
del prices['apple']

print(prices)

#MODIFING
prices['banana'] = prices['banana'] * 1.25

print(prices)

# KEYS
keys = prices.keys()
print(keys)

# VALUES
values = prices.values()
print(values)

# ITEMS
items = prices.items()
print(items)