
# print the words that start with s

def words_with_s( str ):
      words_list = list(str.split())
      new_str = ''

      for word in words_list:
            if word[0] == 's':
                  new_str += word + ' '

      return new_str




print(words_with_s('Print only the words that start with s in this sentence'))