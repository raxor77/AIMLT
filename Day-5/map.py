#example of MAP function

numbers=[2,5,1,8,99]
double_number=list(map(lambda x: x*2, numbers))
print ('\noroginal list')
for num in numbers:
    print(num,end=" ")

print ('\n\ndouble list')
for num in double_number:
    print(num,end=" ")
