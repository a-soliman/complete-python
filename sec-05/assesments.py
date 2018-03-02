
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