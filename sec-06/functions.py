def name_function():
      '''
      This function just says hello
      '''
      print('Hello!')


def dog_check( string ):
      return  'dog' in string.lower()

print(dog_check('there is no  in here'))

# PigLatin
def pig_latin( sentence ):
      words_list = sentence.lower().split()
      vowels = 'aeiou'
      result = ''

      for word in words_list:
            if word[0] in vowels:
                  result += word + 'ay '
            else:
                  starting = ''
                  ending = 'yay '

                  for i in range(0, len(word)):
                        if word[i] not in vowels:
                              starting += word[i]
                        else:
                              result += word[i:] + starting + ending
                              break

      return result.strip()



print(pig_latin('im going to have some apples and coconut'))
