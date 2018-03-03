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

# old_macdonald
# write a function that capitalize the 1st and forth letter of a name

def old_macdonald( name ) :
    if len(name) < 4:
        return name.capitalize()
    
    new_name = ''
    for i in range(0, len(name)):
        if i == 0 or i == 3:
            new_name += name[i].upper()
        else:
            new_name += name[i]
    
    return new_name

print(old_macdonald('oldmacdonald'))