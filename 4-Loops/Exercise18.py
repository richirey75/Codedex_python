# In this lecture I learn about while loop

# In this program there is a while loop to guess a number the user ahs three tries
guess = 0
tries = 0

print('You have three tries!')
while guess != 6 and tries < 3:
  guess = int(input('Guess the number: '))
  tries = tries + 1
  print(tries)
