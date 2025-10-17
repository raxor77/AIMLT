#function without parameters
# def welcome():
#     print("welcome to function")
#     print('Our first define function is Welcome ')
# welcome()

#Function with parameter
# def welcome(nae):
#     print('Welcome to python Mr.\\Mrs.:',nae)

# username=input('Enter Name :\t')
# #function
# welcome(username)

#second eg
def sum(s1,s2):
    return s1+s2

fn=int(input('Enter first Number :'))
sn=int(input('Enter second Number :'))
print(f'result after sum {fn} and {sn} is =\t', sum(fn,sn))