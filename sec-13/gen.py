import random
def gensquares(n):
      for num in range(n):
            yield num**2

for num in gensquares(10):
      print(num)