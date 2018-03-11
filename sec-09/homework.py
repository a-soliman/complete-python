'''
Problem-1
--
handle the exception thrown by the code below by using try and except blocks.
for i in ['a', 'b', 'c']
        print(i**2)
'''

def iterate():
    for i in ['a', 'b', 'c']:
        try:
            print(i**2)
        except:
            print('Can not perform math on str.')
        finally:
            print('Done')

iterate()


'''
Problem-2
--
handle the exception thrown by the code below by using try and except blocks.

x = 5
y = 0

z = x/y
'''

def zero_dev():
    x = 5
    y = 0

    try: 
        z = x /y
    except:
        print('Zero Devition error')
    else:
        print(z)
    finally:
        print('All Done!')

zero_dev()

'''
Problem-2
--
Write a function that asks for an int and prints the square of it. Ise a while
loop with a try, except else block to account for incorrect inputs.

'''

def ask():
    while True:
        try:
            number = int(input('Please provide a number: ').strip())
        except:
            print('That was not a number..')
        else:
            print('Thank you!')
            break

ask()


















