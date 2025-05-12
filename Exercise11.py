# In this lecture I learn about control flow in particular if statements
# I also have a taste of the random and .randint modules

# I make a simple program that simulateds a coin flip

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')