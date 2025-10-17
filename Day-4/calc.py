def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2

print('Welcome to our Calculator')
while True:
    print('Operation selection : \n1.Addition\n2.Substract\n3.Multiply\n4.Divide\n5.Average\n6.Exit')
    op=int(input('enter your operation choice :\t'))
    if(op==6):
        print('Bye')
        break
    if(op>=6) or (op<=0):
        print('Wrong choice only selection 1 to 6 is allowed')
        
    else:
        fnum=float(input('enter first number :\t'))
        snum=float(input('enter first number :\t'))

        if(op==1):
            print(f'Result of Addition ={fnum} and {snum} =',add(fnum,snum))
        if(op==2):
            print(f'Result of Substruc ={fnum} and {snum} =',sub(fnum,snum))
        if(op==3):
            print(f'Result of Multiply ={fnum} and {snum} =',multi(fnum,snum))
        if(op==4):
            print(f'Result of Divide ={fnum} and {snum} =',div(fnum,snum))
        if(op==5):
            print(f'Result of Average ={fnum} and {snum} =',avg(fnum,snum))
    break

