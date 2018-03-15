s = 'hello world3'

print(s.capitalize())
print(s.upper())
print(s.lower())

print(s.count('o'))
print(s.find('h'))

print(s.center(20, '='))

print('hello'.isalnum())
print('hello'.isnumeric())
print('hello'.isalpha())

print('Hello World'.istitle())
print('Hello World'.islower())
print('Hello World'.isupper())

print('hello'.endswith('o'))
print('hello'.startswith('h'))

sentence = 'Hello this is me from the office'
words = sentence.split()
print(words)