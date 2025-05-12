# In this lecture I learn about logical operators

# I create a simple program that checks if you can ride a rollercoaster
# based on your height and credit score

height = int(input('What is your height? '))

credits = int(input('How many credits you have? '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough')
elif height >=137 and credits < 10:
  print('You don\'t have enough credits')
else:
  print('You do not meet the requierments')