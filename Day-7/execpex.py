# try:
#     n1=float(input('Enter Number 1: '))
#     n2=float(input('Enter Number 2: '))
#     total=n1+n2
#     print(f'sum of {n1} and {n2} = {total}')
# except Exception as e:
#     print('ERROR\n',e)
# finally:
#     print('End of Program')

try:
    n1=float(input('Enter Number 1: '))
    n2=float(input('Enter Number 2: '))
    div=n1/n2
    print(f'Div of {n1} and {n2} = {div}')
except Exception as e:
    print('ERROR\n',e)
finally:
    print('End of Program')