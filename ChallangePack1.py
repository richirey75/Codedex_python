# In this challenge pack I will put all challenges in this one file
# do not worry I will separate them with comments like this one 

# Challenge 1
# This program rates the food based on the rating given by the user
rating = float(input('Enter value: '))

if rating > 4.5:
  print('Extraordinary')
elif rating > 4:
  print('Excellent')
elif rating > 3:
  print('Good')
elif rating > 2:
  print('Fair')
else:
  print('Poor')

# Challenge 2
# This program determines the grade of a student based on the input given by the user
grade = int(input('Enter your grade (9-12): '))


if grade == 9:
  print('Freshman')
elif grade == 10:
  print('Sophomore')
elif grade == 11:
  print('Junior')
elif grade == 12:
  print('Senior')
else:
  print('TBD')

# Challenge 3
# This program gives random facts
import random

num = random.randint(0,5)

if num == 0:
  print('Flamingos turn pink from eating shrimp.')
elif num == 1:
  print('The only food that doesn\'t spoil is honey.')
elif num == 2:
  print('Shrimp can only swim backwards.')
elif num == 3:
  print('A taste bud\'s life span is about 10 days')
elif num == 4:
  print('It is impossible to sneeze while sleeping')
elif num == 5:
  print('It is illegal to sing off-key in North Carolina')
else:
  print('Error')

# Challenge 4
# This program checks the season based on the month given by the user
month = int(input('What is the month number? '))

if month == 1 or month == 2 or month == 3:
  print('Winter 🌨️')
elif month == 4 or month == 5 or month == 6:
  print('Spring 🌱')
elif month == 7 or month == 8 or month == 9:
  print('Summer 🌻')
elif month == 10 or  month == 11 or month == 12:
  print('Autumn 🍂')
else:
  print('Invalid')

# Challenge 5
# In this program I ask the user for their weight and planet in order to calculate their weight on that planet
# The planets are:
# 1) Mercury
# 2) Venus
# 3) Mars
# 4) Jupiter
# 5) Saturn
# 6) Uranus
# 7) Neptune

earth_weight = float(input('What is your Earth weight? '))
planet = int(input('What is your planet number(1-6)? '))

if planet == 1:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif planet == 2:
  destiantion_weight = earth_weight * 0.91
  print(destiantion_weight)
elif planet == 3:
  destination_weight = earth_weight * 0.38
  print(destination_weight)
elif planet == 4:
  destination_weight = earth_weight * 2.53
  print(destination_weight)
elif planet == 5:
  destination_weight = earth_weight * 1.07
  print(destination_weight)
elif planet == 6:
  destination_weight = earth_weight * 0.89
  print(destination_weight)
elif planet == 7:
  destination_weight = earth_weight * 1.14
  print(destination_weight)
else:
  print('Invalid planet number')