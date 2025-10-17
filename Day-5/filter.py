#example of FILTER function

# numbers=[2,5,1,8,99]

# print ('\noroginal list: ')
# for num in numbers:
#     print(num,end=" ")

# even_num=list(filter(lambda x: x%2==0, numbers))

# print('\n\nEven Numbers as follow:')
# for num in even_num:
#     print(num,end=" ")

#you have following list

# our_list=[4,2,5,6,7,3,1,10]

# print ('\nour oroginal list: ')
# for num in our_list:
#     print(num,end=" ")

# less_num=list(filter(lambda x: x<5, our_list))  

# print('\n\nNumbers less then 5 are:')
# for num in less_num:
#     print(num,end=" ")

#Example using dictionary

marks={'muhaimin':90,
       'harun':54,
       'salleh':87,
       'maimunah':45,
       'zaitun':78,
       'lina':88,
       'alim':20,
       'zakaria':50}

print('All Students')
for k,v in marks.items():
    print(f'Name: {k} -> Score: {v}')
#print(marks) #this way of simple display also can

pass_student=dict(filter(lambda i: i[1]>50, marks.items()))
print('Pass Students')
for k,v in pass_student.items():
    print(f'Name: {k} -> Score: {v}')
#print(pass_student) #this way of simple display also can

sort_pass=dict(sorted(pass_student.items(), key =lambda x:x[1]))
print('Sort Pass Students Marks Ascending Order')
for k,v in sort_pass.items():
    print(f'Name: {k} -> Score: {v}')
#print(sort_pass)  #this way of simple display also can

sort_pass=dict(sorted(pass_student.items(), key =lambda x:x[1], reverse=True))
print('Sort Pass Students Marks Descending Order')
for k,v in sort_pass.items():
    print(f'Name: {k} -> Score: {v}')
#print(sort_pass)  #this way of simple display also can