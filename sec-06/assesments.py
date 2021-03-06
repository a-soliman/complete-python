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

#------------------------------------
print('='*20)
#------------------------------------

# blackjack
# given thre ints, between 1 and 11, if their sum is less
# than 21, reutrn their sum, if thier sum exceeds 21
# and ther's an eleven, reduce the total sum by 10,
# finally if the sum exceeds 21 return 'BUST 

def blackjack( a, b, c):
    total = a + b + c

    if total < 21:
        return total
    else:
        if a == 11 or b == 11 or c == 11:
            total = total - 10
            if total < 21:
                return total
    
    return 'BUST'


print(blackjack(5,6,7)) # --> 18
print(blackjack(9,9,9)) # --> 'BUST'
print(blackjack(9,9,11)) # --> 19

#------------------------------------
print('='*20)
#------------------------------------

# summer_69
# return the sum of nums in arr, except ignore sections of 
# nums starting with a 6 and extending to the next 9 
# (every 6 will be followed by at least one 9),
# return 0 for no numbers.

def summer_69( arr ):
    total = 0

    if not 6 in arr:
        for num in arr:
            total = total + num
    else:
        start = arr.index(6)
        end = arr.index(9)

        for i in range(0, len(arr)):
            if i < start or i > end:
                total += arr[i]
    
    return total

              



print(summer_69([1,3,5])) # --> 9
print(summer_69([4,5,6,7,8,9])) # --> 9
print(summer_69([2,1,6,9,11])) # --> 14


#------------------------------------
print('='*20)
#------------------------------------

# spy_game
# write  a func that takes in a list of integers and returns True if contains 007 in order

def spy_game( arr ):
    spy = [0,0,7]

    i = 0
    j = 0

    while i < len(arr):
        if arr[i] == spy[j]:
            j = j + 1
            if j  == len(spy):
                return True
        i = i + 1
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

#------------------------------------
print('='*20)
#------------------------------------















