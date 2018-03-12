#two.py
import one

one.func()

print('TOP LEVEL in TWO.py')

if __name__ == '__main__':
      print('TWO.py was called directlly')
else:
      print('TWO.py was imported!')