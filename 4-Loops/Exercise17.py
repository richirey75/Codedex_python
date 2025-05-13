# In this lecture I learn about loops in particular while loop

# In this program I created a PIN machine, it detects if the user entered the correct PIN

print('BANK OF CODÉDEX')

pin = int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. \nEnter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')



