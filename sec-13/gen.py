import random

def gensquares(n):
      for num in range(n):
            yield num**2

for num in gensquares(10):
      print(num)

print('='*20)
def rand_num(low, high, n):
      for x in range(n):
            yield random.randint(low,high)

for num in rand_num(1, 10, 15):
      print(num)