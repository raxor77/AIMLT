#print('we are going to disscuss tuple here')
# subjects=('python','java', 'dotnet', 'sql', 'powerbi' )
# print('\n All Subjects are : ')
# print('Number of Subjects :',len(subjects))
# for sub in subjects:
#     print(sub,end="\u2714")

numbers=(1,2,3,5,2,3,7,88,34,99)
print('Total numbers in Tuple:',len(numbers))
for num in numbers:
    print(num,end='\t')
#tupleName.index(item)will return the index of first occurance of item in tupleName
search_num=int(input('\nEnter number to found out Index : '))
if search_num in numbers:
    print(f'Numbers : {search_num} index : {numbers.index(search_num)}')
else:
    print(f'No such Number {search_num} in our tuple')


# numbers=(1,2,3,5,2,3,7,88,34,99)
# print('Total numbers in Tuple:',len(numbers))
# for num in numbers:
#     print(num,end='\t')
#Frequncy or count in tuple
# search_num=int(input('\nEnter Number to find out Frequency: \t'))
# if search_num in numbers:
#     print(f'Numbers : {search_num} occurs : {numbers.count(search_num)} times')
# else:
#     print(f'No such Number {search_num} in our tuple')