# print('Welcome to day 3- Data Structure')
# print('We will learn \nList \nSet \nTupple \nDictionary/Library')

#first - List Eg.
# my_list=[10, 20, 30, 'python',None,True,12.45]
# print('Number of list in my items are :', len(my_list))
# for item in my_list:
#     print(item)

# print('second example of list')
# emp=['abdul', 'daud', 'fatimah', 'ramlan', 'yusuf', 'siti', 'arun', 'albert', 'john']
# print('Numbers of Employes :', len(emp))
# print('All Employees :')
# for employes in emp:
#     print(employes, end=" ")

    

#second - Sort Eg.
#emp.sort()
# print('\n List after sortting:')
# for e in emp:
#     print(e, end=' ')

# #reverse order
# emp.reverse()
# print('\n List after reverse sortting:')
# for e in emp:
#     print(e, end=' ')

#append, remove, pop insert method

# emp=['Abdul', 'Daud', 'Fatimah', 'Ramlan', 'Zara', 'Yusuf', 'Siti', 'Arun', 'Albert', 'John']
# print('Numbers of Employes :', len(emp))
# print('All Employees :')
# for employes in emp:
#     print(employes, end=" ")

# #append = Adds the item to the end of list.
# # newemp=input("\n Enter New Employe name to add in the list :")
# # emp.append(newemp)
# # print("\nAfter adding new employee, Number of Employees are :", len(emp))
# # for employes in emp:
# #     print(employes, end=" ")

# #insert = Adds the item in the list
# newemp=input("\n Enter New Employe name to add in the list :")
# pos=int(input("enter position where you want to insert inside list: \t"))
# emp.insert(pos,newemp)
# print("\nAfter adding new employee, Number of Employees are :", len(emp))
# for employes in emp:
#     print(employes, end=" ")

#remove = Delete from list
# emp=['Abdul', 'Daud', 'Fatimah', 'Ramlan', 'Zara', 'Yusuf', 'Siti', 'Arun', 'Albert', 'John']
# print('Numbers of Employes :', len(emp))
# print('All Employees :')
# for employes in emp:
#     print(employes, end=" ")
# delinput=input("\nName to Remove from Employees List :\t")
# if delinput in emp:
#     emp.remove(delinput)
#     print(f"Number of Employees after Remove {delinput} in List are : ",len(emp))
#     for employes in emp:
#         print(employes,end=" ")
# else:
#     print("not name in list")
#     print("\u2764")

#Pop() eg
# emp=['Abdul', 'Daud', 'Fatimah', 'Ramlan', 'Zara', 'Yusuf', 'Siti', 'Arun', 'Albert', 'John']
# print('Numbers of Employes :', len(emp))
# print('All Employees :')
# for employes in emp:
#     print(employes, end=" ")
# #List Name.pop(index): Delete elementat givenindex and return its value
# del_index=int(input("Enter Index to Pop Item :\t"))
# print('Pop Result :',emp.pop(del_index))

# print(f"Number of Employees after Remove {del_index} in List are : ",len(emp))
# for employes in emp:
#     print(employes,end=" ")


emp=['Abdul', 'Daud', 'Fatimah', 'Ramlan', 'Zara', 'Yusuf', 'Siti', 'Arun', 'Albert', 'John']
print('Numbers of Employes :', len(emp))
print('All Employees :')
for employes in emp:
    print(employes, end=" ")
print('\nfirst element in the list',emp[0])
print('2nd last element in the list',emp[-2])
print('last element in the list',emp[-1])