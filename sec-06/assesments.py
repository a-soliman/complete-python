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

#------------------------------------
print('='*20)
#------------------------------------
# Animal crackers:
# write a func takes 2 string and return true if both words begin with same letter

def animal_crackers( string1, string2):
    return string1[0].lower() == string2[0].lower()


print(animal_crackers('Levis', 'Llama'))
print(animal_crackers('Levis', 'kangaroo'))

#------------------------------------
print('='*20)
#------------------------------------

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


#------------------------------------
print('='*20)
#------------------------------------


# given a sentence, retur a sentence with the words reversed

def master_yoda( sentence ):
    words_list = sentence.split()
    reversed_sen = ''
    i = len(words_list)-1

    while i >= 0:
        reversed_sen += words_list[i]
        
        if i != 0:
            reversed_sen += ' '
        i = i -1

    return reversed_sen

print(master_yoda('I am home'))
print(master_yoda('we are ready'))

#------------------------------------
print('='*20)
#------------------------------------


# almost_there 
# Given an int n, return True if n is within 10 of either 100 or 200.
def almost_there( n ):
    return ( n >= 90 and n <= 110) or (n >= 190 and n <= 210)


print(almost_there(90)) # True
print(almost_there(104)) # True
print(almost_there(150)) # False
print(almost_there(209)) # True

#------------------------------------
print('='*20)
#------------------------------------


# laughter
# write a function that counts the number of times a given pattern appers in a string, including overlap

def laughter( pattern, string):
    count = 0

    for i in range( 0, len(string)):
        if string[i] == pattern[0]:
            if string[i: i+ len(pattern):] == pattern:
                count = count + 1
    return count

print(laughter('hah', 'hahahah')) # --> 3

#------------------------------------
print('='*20)
#------------------------------------

# paper_doll
# given a string return string where for every char in the original there are thre chars.reversed

def paper_doll( string ):
    new_str = ''

    for letter in string:
        new_str += letter *3
    return new_str

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))



















