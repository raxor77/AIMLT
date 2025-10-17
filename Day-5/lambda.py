# def add(a,b):
#     total=a+b
#     return total

# result=add(52,41)
# print(result)


# addition = lambda a,b : a+b
# substruc = lambda a ,b : a-b
# multi = lambda a,b :a*b
# div = lambda a,b:a/b
# avg =lambda a, b : (a*b)/2

# num1 =int(input('enter 1st number:\t'))
# num2 =int(input('enter 2nd number:\t'))

# print(f'addition result',addition(num1,num2))
# print(f'sub result',substruc(num1,num2))
# print(f'multply result',multi(num1,num2))
# print(f'devide result',div(num1,num2))
# print(f'average result',avg(num1,num2))

#2nd example to find Odd or even number

check_odd=lambda n: "odd number" if n%2==1 else "even number"
num1=int(input('Enter Number to check odd or even :\t'))
print(check_odd(num1))


