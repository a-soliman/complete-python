# def func():
#       return 1

# func()

# def hello():
#       return 'Hello'

# greet = hello


# del hello
# print(greet())

# nested func

# def hello(name='Ahmed'):
#       print('This is hello() has been excuted')

#       def greet(name):
#             return '\n this is the greet() from hello(), saying hello {}'.format(name)
      
#       def welcome():
#             return '\n this is welcome() inside hello()'
      
#       print('I am going to return a function')

#       if name == 'Ahmed':
#             return greet(name)
#       else:
#             return welcome()

# print(hello('zzz'))


# passing a func as param

def hello(name='Ahmed'):
      return 'Hey {}'.format(name)

def other_func(func):
      print('This is the other_func()')
      print(func())

other_func(hello)
