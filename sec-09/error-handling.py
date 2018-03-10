def add ( n1, n2 ):
    return n1 + n2


add(10, 20)

num1 = 10
num2 = input('Please provide anumber: ')

try:
    result = add(num1, num2)
except:
    print('There was an error!')
else:
    print('add went well!')
    print(result)