from ourpack import calc
while True:
    try:
        fnum=float(input("Enter Number :\t"))
        snum=float(input("Enter Number :\t"))

        op=input('Choose operation +,-,x,/,a :\t')
        if (op=='+'):
            print('Result:\t',calc.add(fnum,snum))
        elif (op=='-'):
            print('Result:\t',calc.sub(fnum,snum))
        elif (op=='x'):
            print('Result:\t',calc.multi(fnum,snum))
        elif (op=='/'):
            print('Result:\t',calc.div(fnum,snum))
        elif (op=='a'):
            print('Result:\t',calc.avg(fnum,snum))

        else:
            print('wrong operation choice')
    except ZeroDivisionError as ze:
        print('Division by 0 not Allowed',ze)
    except ValueError as ve:
        print('Error in Value', ve)
    except Exception as e:
        print('Error:',e)
    finally:
        print("end")
    choice=input('Do you want to Continue? \nIf yes Press y or Press Any keys to Exit :').lower()
    if (choice!='y'):
        print('bye!')
        break