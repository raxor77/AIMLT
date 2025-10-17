def check_odd_even(num):
    if(num%2==0):
        print(f'Even Number {num}')
    else:
        print('Odd Number ',num)
given_num=int(input('Enter Number :\t'))
check_odd_even(given_num)