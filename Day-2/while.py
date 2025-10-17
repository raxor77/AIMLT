# Continue eg.
# ourNum=1
# print('Printing Numbers from 1 to 100')
# while(ourNum<=100):
#     print(ourNum, end=(" "))
#     ourNum+=1

#Break eg.
# ourNum=1
# print('Printing Numbers from 1 to 100 before we got the numbers divisible by 11')
# while(ourNum<=100):
#     if(ourNum%11==0):
#         break
#     print(ourNum, end=(" "))
#     ourNum+=1

#Continue "while" eg.
# ourNum=1
# print('Printing Numbers from 1 to 100 those are not divisible by 11')
# while(ourNum<=100):
#     if(ourNum%5==0):
#         ourNum+=1
#         continue
#     print(ourNum, end=("\t"))
#     ourNum+=1

#continue using "for" eg.
# for i in range(1,101):
#     if(i%5==0):
#         continue
#     print(i,end="\t")

#Looping enter Password
# correctpass="01"
# while True:
#     pwd=input('Please Enter Password : ')
#     if(correctpass==pwd):
#         print('Welcome Back, Access Granted')
#         break
#     else:
#         print('Wrong Password, Try Again')
# print('Initializing Sequence')

# #Looping enter Password 3 times
# correctpass="01"
# counter=1
# while True:
#     pwd=input('Please Enter Password : ')
#     if(correctpass==pwd):
#         print('Welcome Back, Access Granted')
#         print('Initializing Sequence')
#         break
#     else:
#         print(f'Wrong Password, Try Again attemp {counter}')
#         counter+=1
#         if(counter>3):
#             print("attempted more then 3 times")
#             print('wait for 24h')
#             break
        

correctpass="01"
counter=1
while True:
    pwd=input('Please Enter Password : ')
    if(correctpass==pwd):
        print('Welcome Back, Access Granted')
        print('Initializing Sequence')
        break
    else:
        print(f'Wrong Password, Try Again attemp {counter}')
        counter+=1
        if(counter>3):
            print("attempted more then 3 times")
            print('wait for 24h')
            import time
            start_time = time.perf_counter()
            for start_time in range(3600):
                pass
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.4f} seconds")
            break
            