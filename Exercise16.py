# In this lecture I did a recap of the previous lecture

# In this program I ask the user questions and based on the answers I give them a score
# the score determines if they are a good candidate for the houses of Hogwarts School of Witchcraft and Wizardry
# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


q1 = int(input('Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n'))

if q1 == 1:
  Gryffindor, Ravenclaw = Gryffindor + 1, Ravenclaw + 1
elif q1 ==2:
  Hufflepuff, Slytherin = Hufflepuff + 1, Slytherin + 1
else:
  print('Wrong input')

print("*********************************")
print(f'Gryffindor: {Gryffindor}')
print(f'Ravenclaw: {Ravenclaw}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Slytherin: {Slytherin}')

q2 = int(input('When I\'m dead, I want to people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n'))

if q2 == 1:
  Hufflepuff = Hufflepuff + 2
elif q2 == 2:
  Slytherin = Slytherin + 2
elif q2 == 3:
  Ravenclaw = Ravenclaw + 2
elif q2 == 4:
  Gryffindor = Gryffindor + 2
else:
  print('wrong input') 
print("***************************")
print(f'Gryffindor: {Gryffindor}')
print(f'Ravenclaw: {Ravenclaw}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Slytherin: {Slytherin}')


q3 = int(input('Which kind of instrument most pleases your ear? \n 1) The Violin \n 2) The Trumpet \n 3) The Piano \n 4) The drum \n'))

if q3 == 1:
  Slytherin = Slytherin + 4
elif q3 == 2:
  Hufflepuff = Hufflepuff + 4
elif q3 == 3:
  Ravenclaw = Ravenclaw + 4
elif q3 == 4:
  Gryffindor = Gryffindor + 4
else:
  print('Wrong input') 

print("*************************************")
print(f'Gryffindor: {Gryffindor}')
print(f'Ravenclaw: {Ravenclaw}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Slytherin: {Slytherin}')

print('**********')
if Gryffindor > Slytherin and Gryffindor > Hufflepuff and Gryffindor > Ravenclaw:
  print('Gryffindor')
elif Slytherin > Hufflepuff and Slytherin > Ravenclaw:
  print('Slytherin')
elif Hufflepuff > Ravenclaw:
  print('Hufflepuff')
else:
  print('Ravenclaw')



