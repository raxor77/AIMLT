class invalidmark(Exception):
    pass
def check_mark(mark):
    if(mark<0):
        raise invalidmark('Mark should not be negative')
    elif(mark>50):
        raise invalidmark('Mark should be between 0 to 50')
    else:
        print(f'you have enter {mark} ')
