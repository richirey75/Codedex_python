# In this lecture I recap the previous lecture

# In this program I print 'frizz' and 'buzz' for multiples of 3 and 5 respectively
# and 'frizzbuzz' for multiples of both 3 and 5
# I also print the numbers from 1 to 100

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
  elif num % 3 == 0:
    print('Fizz')
  elif num % 5 == 0:
    print('Buzz')
  else:
    print(num)
# the if statement will always be looked while the elif could be skip if the first if
# was taken in to account 
