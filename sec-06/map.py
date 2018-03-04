def square(num):
    return num **2

nums = [1,2,3,4,5]

l = list( map( square, nums))

print(l)