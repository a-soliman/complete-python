
# print the words that start with s

def words_with_s( str ):
      words_list = list(str.split())
      new_str = ''

      for word in words_list:
            if word[0] == 's':
                  new_str += word + ' '

      return new_str

print(words_with_s('Print only the words that start with s in this sentence'))

#---------------------------------------------------
print( '-'*20)
#---------------------------------------------------

# use rangge to print out all the even nums from 0 to 10

l1 = [ num for num in range(0,11) if num %2 == 0 ]
print(l1)

#---------------------------------------------------
print( '-'*20)
#---------------------------------------------------

# use list-comprehenssion to create a list bet 1:50 that are dev by 3
l2 = [ num for num in range(1, 51) if num %3 == 0]
print(l2)

#---------------------------------------------------
print( '-'*20)
#---------------------------------------------------

# Go through the string below and if the length of the word is even print even

st = 'Print even word in this sentence that has an even number of letters'

l3 = st.split()

for word in l3:
      if len(word) % 2 == 0:
            print('Even')
      else:
            print('ODD!')

#---------------------------------------------------
print( '-'*20)
#---------------------------------------------------

# FizzBuzz

for i in range(0, 101):
      if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
      elif i % 5 == 0:
            print('Buzz')
      elif i % 3 == 0:
            print('Fizz')
      else:
            print(i)

#---------------------------------------------------
print( '-'*20)
#---------------------------------------------------

# use list-comprehension to create a list of every 1st letter of the string below

st2 = 'Create a list of the first letters of every word in this string'
l5 = st2.split()
l6 = [ x[0] for x in st2.split() ]
print(l6)