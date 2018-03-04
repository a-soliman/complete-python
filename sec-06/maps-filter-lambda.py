def square(num):
    return num **2

nums = [1,2,3,4,5]

l = list( map( square, nums))

print(l)

def splicer( string ):
    if len(string)%2 == 0:
        return 'Even'
    else:
        return string[0]

sentence = 'Hello this is ahmed saying hello'
l2 = list( map(splicer, sentence.split()))
print(l2)

# Filter

def check_even(num):
    return num % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,10]

new_list = list(filter(check_even, nums))

print(new_list)

def starts_with_a( name ):
    return name[0].lower() == 'a'

names = ['Ahmed', 'Mike', 'Jack', 'Adam']

names_with_a = list(filter(starts_with_a, names))

print(names_with_a)