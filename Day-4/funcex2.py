#default parameter in functions
# def inf(id,name,city='KL'):
#     print(f'detail as follow\n ID : {id} Name : {name} City : {city}')

# inf(1, 'hadi', 'penang')
# inf(45,'daud')
# inf(56,'rashidah')

#we want to create a single method that can able to add 2 numbers,3 numbers, 4numbers and 5 numbers
#and return correct total
# def count(n1,n2=0,n3=3,n4=0,n5=0): #if (n1,n2,n3,n4,n5) without value become error for below print
#     return n1+n2+n3+n4+n5

# print('result',count(5,6,4,4))
# print('result',count(5,6))

# def count(*args): 
#     return sum(args)

# print('sum of numbers 1,11,34 is :\t',count(1,11,34))
# print('sum of numbers 5,61,34,77,40 is :\t',count(5,61,34,77,40))
# print('sum of numbers 100,11,34,400,236,12,800,44 is :\t',count(100,11,34,400,236,12,800,44))


print('Maximum Eg')
print('sum of numbers 1,11,34 is :\t',max(1,11,34))
print('sum of numbers 5,61,34,77,40 is :\t',max(5,61,34,77,40))
print('sum of numbers 100,11,34,400,236,12,800,44 is :\t',max(100,11,34,400,236,12,800,44))
print('Minimum Eg')
print('sum of numbers 1,11,34 is :\t',min(1,11,34))
print('sum of numbers 5,61,34,77,40 is :\t',min(5,61,34,77,40))
print('sum of numbers 100,11,34,400,236,12,800,44 is :\t',min(100,11,34,400,236,12,800,44))