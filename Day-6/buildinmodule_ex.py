import math
import random
import inspect
# #example of cuberoot
# my_num=int(input('Enter Number to find Cube root:\t'))
# print(f'Cube root of {my_num} is',math.cbrt(my_num))

# #example of squareroot
# my_num=int(input('Enter Number to find Square root:\t'))
# print(f'Square root of {my_num} is',math.sqrt(my_num))

# #Get lucky number 1 to hundred
# print('Your lucky number from 1 to 100 is :\t', random.randint(1,100))

#to check function inside module
# function = inspect.getmembers(math, inspect.isbuiltin)
# print(function)
# for n, func in function:
#     print(n)

print('sin 90 is:',math.sin(90))
print('coc 90 is:',math.cos(90))
print('sin 90 is:',math.tan(90))
deg=int(input('Degree to find out cos :\t'))
print(f'Cos {deg}degree is:', math.cos(deg))