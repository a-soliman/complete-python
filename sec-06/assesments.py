# lesser of two even:
# return the lesser of two given nums if both are even
# return the greater num of one or more are odd

def lesser_of_two( a,b ):
    greater = max(a,b) 
    lesser = min(a,b)

    if a % 2 == 0 and b % 2 == 0:
        return lesser
    else: 
        return greater

print(lesser_of_two(2,4))
print(lesser_of_two(2,5))

print('='*20)

# Animal crackers:
# write a func takes 2 string and return true if both words begin with same letter

def animal_crackers( string1, string2):
    return string1[0].lower() == string2[0].lower()


print(animal_crackers('Levis', 'Llama'))
print(animal_crackers('Levis', 'kangaroo'))