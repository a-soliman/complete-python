def myfunc(a,b):
    # Returns 5% of the sum of a and b.
    return sum((a, b)) * 0.05


print(myfunc(40,60))


def myfunc2( *args ):
    return sum(args) * 0.05

print(myfunc2(40,60,100,100))

def sum_nums( *args ):
    # Returns the sum of the given arguments
    return sum(args)

print(sum_nums(1,2,3,4,5,6,78,9))

#===================================
print('='*10)
#===================================

#**kwargs
def myfunc3( **kwargs ):
    print('His name is {}, he is {} years old, and he lives in {}.'.format(kwargs['name'], kwargs['age'], kwargs['city']))

myfunc3(name='Ahmed', age=30, city='San Fran')

#===================================
print('='*10)
#===================================

# *args + **kwargs
def func4( *args, **kwargs ):
    print('I need to buy {} {}.'.format(args[0], kwargs['food']))


func4(12,13,14, fruit="Banana", food="egg")
