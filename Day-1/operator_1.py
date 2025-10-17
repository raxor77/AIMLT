# #Assignment operators : =, +=, -=
# # price=float(input("Enter product Price : "))
# # discount=price*0.10
# # disprice=price-discount
# # print(f" Price: {price} \n Discount: {discount} \n Discounted Price: {disprice}")

# # salary=8000.50
# # bonus=1000.00
# # print(f"Salary {salary}, and Bonus {bonus}")
# # salary+=bonus
# # print("Salary with Bonus",salary)

# # salary=8000.50
# # tax=200.60
# # print(f"Salary {salary}, and Tax {tax}")
# # salary-=tax
# # print("Salary deduct Tax",salary)

# # #Comparison operators : ==, >, >=, <, != etc.
# # age=int(input("Enter Your Age :"))
# # if(age>=18):
# #     print("You Are Eligible to Vote")
# # else:
# #     print("Sorry, You Are Not Eligible to Vote")
# # print('End of Program')

# # marks=int(input("Enter Marks Percentage Without '%' sign "))
# # if(marks<30):
# #     print("Fail Exam")
# # else:
# #     print("You Pass!!")

# accesscode=input("Enter Access Code :\n")
# if(accesscode!="wes1234") :
#     print("Invalid Code")
# else :
#     print("Welcome Back Sir!")

# accesscode=input("Enter Access Code :\n")
# if(accesscode=="wes1234") :
#     print("Welcome Back Sir!")
# else :
#     print("Invalid Code")

#Logical operators : and, or, not. 
# phyMarks=int(input("Enter marks obtain in Physics : "))
# cheMarks=int(input("Enter marks obtain in Chemistry : "))
# addmathMarks=int(input("Enter marks obtain in Add Math : "))
# if((phyMarks>=50) and (cheMarks>=60) and (addmathMarks>=55)):
#     print("You are eligible to sit for Final Exam")
# else:
#     print("Sorry you need retake again")

# idproof=input("Enter ID Proof You Have : \t")
# if ((idproof=="Passport") or (idproof=="License") or (idproof=="NRIC")) :
#     print(f"Valid ID {idproof} Accept Here")
# else:
#     print("Only Passport, License, and  NRIC are accepted as Identity Proof")
#     print(f"{idproof} not valid here")

# addmathMarks=int(input("Enter marks obtain in Add Math : "))
# gapyear=int(input("Enter year gap : "))
# if((addmathMarks>=55) or (gapyear == 0)):
#     print("Not eligible for BTech")
# else:
#     print("eligible for BTech")

name=input("Enter Name")
if(not name):
    print("username availble")
else:
    print("No username")