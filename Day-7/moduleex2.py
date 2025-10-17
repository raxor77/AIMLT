import datetime
import inspect

print('\nAll Classes inside datetime module')
dtclasses = inspect.getmembers(datetime, inspect.isclass)
for n, func in dtclasses:
    print(n,end=' / ')

print('\nAll functions inside datetime.datetime class')
functions = inspect.getmembers(datetime.datetime, inspect.isbuiltin)
for n, func in functions:
    print(n,end=' / ')


#today date
print('\nToday is (Date):',datetime.date.today())
# or print like this
print('\n----Today date----')
print(datetime.date.today())

#Current date/time
print('\nCurrent Day Time:',datetime.datetime.now()) #<--Date  and time
print('\n----current time----') #<- time only
print(datetime.datetime.now().time())

#Another way to display < using str 
cttime=datetime.datetime.now().time()
formattedtime=datetime.datetime.now().strftime('%I :%M :%S %p')
frmtddate=datetime.date.today().strftime("%B %d, %Y")
print('display formaatted current date:',frmtddate)
print('display current time:',cttime)
print('display formatted current time:',formattedtime)
