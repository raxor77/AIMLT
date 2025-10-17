# def display():
#     print('Welcome Recap of Function')


# def welcome(name):
#     print('Welcome Mr.//Mrs.',name)

# def cube(num):
#     cube_num=num*num*num
#     print(f'Cube of given number: {num} is =\t {cube_num}')

# def sq(num):
#     return num*num

# # welcome('dan')
# # display()
# # my_num=int(input('Enter the number to find out Cube =\t'))
# # cube(my_num)

# username=input('Enter Username :\t')
# sq_num=int(input('Enter number to find out square :\t'))
# my_num=int(input('Enter the number to find out Cube :\t'))

# welcome(username)
# cube(my_num)
# print(f'Square of given : {sq_num} is =\t',sq(sq_num))

# def bonsalary(num):
#     return num*0.10

# my_salary=float(input('Enter Salary :\t'))
# bonus=bonsalary(my_salary)
# print(f'My Salary in {my_salary} with bonus {bonus})')
# print(f'My total salary is :',my_salary+bonus)

def bonsalary(salary):
    bonus=salary*0.10
    print(f'salary {salary}, bonus {bonus}')

my_sal=float(input('Enter salary to Find out bonus :\t'))
bonsalary(my_sal)
#print(f'Salary with bonus') <-cannot because bonus cannot define