import math
import inspect
import datetime
# num=int(input('enter numbers to find Square Root :\t'))
# print(f'Square root of {num}\t',math.sqrt(num))

# functions = inspect.getmembers(math, inspect.isbuiltin)
# print('All function in math module')
# for n, func in functions:
#     print(n,end=' ')


# print('Today is (Date):',datetime.date.today())

# dtclasses = inspect.getmembers(datetime, inspect.isclass)
# print('All Classes inside datetime module')

# for n, func in dtclasses:
#     print(n)

# print('All functions inside datetime.date class')

# functions = inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n, func in functions:
#     print(n)

# example for random module
# import random

# print('Your lucky Number from 1 to 1000 is: ',random.randint(1,1000))

# #also can be write like below
# print('random number from 1 to 1000')
# print(random.randint(1,1000))

#ooyou
import random
def winner():
    name=input('Enter Name:\t')
    luckynumber=(random.randint(1,100))
    print(f'welcome Mr.\\Mrs.{name}, your coupon number is : {luckynumber} ')
    if (luckynumber==1):
        print('Wou have won pencil')
    elif(luckynumber==2):
        print('Wou have won chair')
    elif(luckynumber==16):
        print('Wou have won Proton X70')
    elif(18<=luckynumber<=25):
        print('Wou have won chair')
    else:
        print('hazure')

