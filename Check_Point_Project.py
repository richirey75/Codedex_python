import math

print('---------------------------------\n')
print('WELCOME TO THE SHAPE CALCULATOR \U0001F916 \n')
print('---------------------------------\n')
print('Here are your options\n')

while True:
    print('1) Square\n\n2) Rectangle\n\n3) Triangle\n\n4) Circle\n\n5) Quit\n ')

    order = int(input('Your choice:\n '))
    quit = True


    if order == 1:
        side = int(input('what is the number of your side? \n'))
        area_square = side ** 2
        print(f'The area of your rectangle is {area_square}\n')

    elif order == 2:
        base = int(input('What is your base? \n'))
        height = int(input('What is your height? \n'))
        area_rectangle = base * height
        print(f'The area of the rectangle {area_rectangle}\n')

    elif order == 3:
        base = int(input('what is your base? \n'))
        height = int(input('what is your height? \n'))
        area_triangle = (base * height) / 2
        print(f'The are of the triangle {area_triangle}\n')

    elif order == 4:
        pi_value = math.pi
        radius = int(input('what is your radius? \n'))
        area_circle = pi_value * (radius ** 2)
        print(f'The area of a circle is {area_circle}\n')
    
    elif order == 5:
        print('Goodbye')
        break
    else:
        print('The choice you picked was invalid, make you sure to use the 1-5 keys \N{grinning face}\n')





