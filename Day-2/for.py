# eg of range
#  print("Number 0 to 9")
# for i in range(10):
#     print(i)

# eg of range
# print("Printing Numbers 1 to 10")
# for i in range(1,11):
#     print(i)

# eg of range
# print("Printing Numbers 1 to 10")
# for i in range(10):
#     print(i+1)

# eg of range
# for i in range(5,11):
#      print(i)

# eg of range
# for range in range(100):
#      print(range+10, end=" ")  #space added

#Eg of list
# students=['amir', 'syed', 'ahmad', 'hashim', 'maimun']
# for s in students:
#      print(s,end=" ")

#Eg of list
# products=['Syampoo', 'FaceScrub', 'facial Wash', 'Sunscreen', 'Hair Oil', 'Lip Balm', 'Nail Polisher']
# for items in products:
#      print(items,end=", ")

#Eg of string
# for ch in 'Nextpert Academy':
#      print(ch,end="-> ")

#Eg of string
# name=input('Enter Your Name : \t')
# print('Characters of Your Name as follows : \n')
# for ch in name:
#      print(ch)

# # eg of range
# num=int(input('enter numbers : \t'))
# print(f'table of numbers {num}as follow : \n')
# for i in range(1,11):
#      print(f'{num}*{i}=\t{num*i}')

#A tuple is an immutable data type in python
#eg:
players=('Lionel Messi', 'Christiano Ronaldo', 'Pele', 'Deigo')
for player in players:
    print(player)

players=('Lionel Messi', 'Christiano Ronaldo', 'Pele', 'Deigo')
for player in players:
    print(player[0])  #this is tuple will show only first letter of names

players=('Lionel Messi', 'Christiano Ronaldo', 'Pele', 'Deigo')
for player in players:
    print(player[0], end='\t') #this tupple and list