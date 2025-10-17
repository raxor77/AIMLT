class invalidage(Exception):
    pass
def check_age(age):
    if(age<=0):
        raise invalidage('Age Should not be Negative')
    if(age<18):
        raise invalidage('You are below 18')
    if(age>=80):
        raise invalidage('too old for employment')
    else:
        print(f'Age {age} is valid age for employment')

try:
    userage=int(input('Enter your age :'))
    check_age(userage)
except invalidage as inv:
    print('Invalid Age : ',inv)
except Exception as er:
    print('error!!!',er)