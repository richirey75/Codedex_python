# In this lecture I learn about string interpolation and how to use it to format strings in Python

# In this program I loop in range of 99-0 lyrics of the song "99 Bottles of Beer on the Wall"

for i in range(99, 0, -1):
  print(f'\n {i} bottles of beer on the wall')
  print(f'\n {i} bottles of beer')
  print(f'\n Take one down, pass it around')
  print(f'\n {i-1} bottles of beer on the wall')
