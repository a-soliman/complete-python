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