# import datetime
# import inspect

# print('show All classes of datetime module')
# dtclasses = inspect.getmembers(datetime,inspect.isclass)
# for n, func in dtclasses:
#     print(n)

# print('show All classes of datetime.date classes')
# functions = inspect.getmembers(datetime.date,inspect.isbuiltin)
# for n, func in functions:
#     print(n)

# print('show All classes of datetime.time classes')
# time = inspect.getmembers(datetime.time,inspect.isbuiltin)
# for n, func in time:
#     print(n)

# print('Today is (date) :',datetime.date.today())
# #print('Today is (date) :',datetime.time.fromisoformat())


import os
listDirs=os.listdir()
for list in listDirs:
    print(list)
