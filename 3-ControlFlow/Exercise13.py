# In this lecture we learn about relatioinal operators
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# I create a ph scale using if statements
ph = int(input('Give me a value 0-14? '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")
