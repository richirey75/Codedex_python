# In this lecture I learn about modules 

# I create a simple magic 8 ball program using the random module
# You ask a question and the program gives you a random answer from 1-9 

import random

question = input('Question: ')
random_num = random.randint(1, 9)

if random_num == 1:
  print('Magic 8 Ball: Yes - definitely.')
elif random_num == 2:
  print('Magic 8 Ball: It is decidedly so.')
elif random_num == 3:
  print('Magic 8 Ball: Without a doubt.')
elif random_num == 4:
  print('Magic 8 Ball: Reply hazy, try again.')
elif random_num == 5:
  print('Magic 8 Ball: Ask again later.')
elif random_num == 6:
  print('Magic 8 Ball: Better not tell you now.')
elif random_num == 7:
  print('Magic 8 Ball: My sources say no.')
elif random_num == 8:
  print('Magic 8 Ball: Outlook not so good.')
elif random_num == 9:
  print('Magic 8 Ball: Very doubtful.')
else:
  print('errror')

