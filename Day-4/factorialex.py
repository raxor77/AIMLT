# def factorial(num):
#     if ((num==0) or (num==0)):
#         return 1
#     else:
#         return num*factorial(num-1)
# num=int(input('enter a number to find out factorial: '))
# print(f'factorial of {num} is:', factorial(num))

#write python function which convert inches to cm
#1inch =2.5cm
# def inch(In):
#     return In*2.5

# inches=float(input('Enter how many Inches: \t'))
# #print(f'Inches {inches} =', inch(inches))   <also can
# print(f'{inches} inches equal to {inch(inches)} centimeter')


#Function to gen table
def gen_table(num):
    for i in range(1,20):
        print(f'{num}*{i} =\t{(num*i)}')
number=int(input('Enter Number to find out table :\t'))
gen_table(number)