import datetime

t = datetime.time(5,25,1)
print(t)
print(t.minute)

today = datetime.date.today()
print(today)

def get_birth_year( age ):
      try:
            num_age = int(age.strip())
      except:
            return False
      
      current_year = datetime.date.today().year
      return current_year - num_age


print(get_birth_year('aaa'))