def num(n1,n2,n3):
    return max(n1,n2,n3)

n1=float(input('Please input first num : '))
n2=float(input('Please input second num : '))
n3=float(input('Please input third num : '))

print(f'from {n1}, {n2}, {n3} max are : ',max(n1,n2,n3))

# nums = [float(input(f"Enter number {i+1}: ")) for i in range(3)]
# print("The greatest number is:", max(nums))