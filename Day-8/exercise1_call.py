from ourpack import mark
while True:
    try:
        usermark=int(input('Enter your Mark :'))
        mark.check_mark(usermark)
    except mark.invalidmark as inv:
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