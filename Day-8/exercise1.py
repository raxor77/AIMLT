class invalidmark(Exception):
    pass
def check_mark(mark):
    if(mark<0):
        raise invalidmark('Mark should not be negative')
    elif(mark>50):
        raise invalidmark('Mark should be between 0 to 50')
    else:
        print(f'you have enter {mark} ')

while True:
    try:
        usermark=int(input('Enter your Mark :'))
        check_mark(usermark)
    except invalidmark as inv:
        print('Invalid Mark : ',inv)
    except Exception as er:
        print('error!!!',er)
    else:
        print('Recorded')
        break
    choice=input('do you want to reenter :').lower()
    if (choice!='y'):
        print('bye')
        break