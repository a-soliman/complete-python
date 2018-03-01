my_set = set()

# ADDING
my_set.add(1)
my_set.add(2)

# Conflicting
my_set.add(2)
print(my_set)

# useCase

def get_unique( list ):
    new_set = set()

    for value in list:
        new_set.add(value)

    return new_set

print(get_unique([1,2,1,2,5,4,6,4,5]))