import re

patterns = ['term1', 'term2']

text = 'this is a string with term1, but not the other term'

for pattern in patterns:
      print ('Serching for {} in: {}'.format(pattern, text))

      # Check for match
      if re.search(pattern, text):
            print ('\n')
            print ('Match was found. ')
      else:
            print ('\n')
            print ('(No Match was found ')

print('='*20)

#Split_term()

def split_domain():
      email = input('Please enter your email address: '.strip())

      split_term = '@'
      refactored = re.split(split_term, email)

      return refactored[1]

print(split_domain())
