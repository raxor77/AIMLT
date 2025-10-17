# class acc:
#     def __init__(self,ac_hol,balance):
#         self.ac_hol=ac_hol
#         self.bal=balance
#     def deposit(self, amount):
#         self.bal=amount
#         print('Balance after deposit',self.bal)
#     def withdraw(self,amount):
#         if(self.bal>=amount):
#             self.bal-=amount
#             print('Balance after Withdraw',self.bal)
#         else:
#             print('insufficient amount in Account')
#             print('Transaction Failed')
#     def show(self):
#         print(f'Account Holder Name :{self.ac_hol} \nAccount Balance :{self.bal}')

# # ac1=acc('sulaiman',4500)
# # ac2=acc('danish',600)
# # ac1.show()
# # ac2.show()
# ac1=acc('Sulaiman', 7000)
# ac1.show()
# wamount=float(input('Enter Amount to withdraw :'))
# ac1.withdraw(wamount)


# #Balance call
# class acct:
#     def __init__(self, balance, ac_holder):
#         self.balance=balance
#         self.ac_holder=ac_holder

#     def get_balance(self):
#         return self.balance
    
# a1=acct(100000,'said')
# a1.balance()
    

##More example
class acc:
    def __init__(self,ac_hol,balance):
        self.ac_hol=ac_hol
        self.bal=balance

    def deposit(self, amount):
        self.bal+=amount
        print('Balance after deposit',self.bal)

    def withdraw(self,amount):
        if(self.bal>=amount):
            self.bal-=amount
            print('Balance after Withdraw',self.bal)
        else:
            print('insufficient amount in Account')
            print('Transaction Failed')

    def show(self):
        print(f'Account Holder Name :{self.ac_hol} \nAccount Balance :{self.bal}')


ac1=acc('ghani',5000)
ac1.show()
print('Please Choose\n 1.Deposit  2.Withdraw  3.Balance' )

choice=int(input())
# If example
if (choice==1):
    damount=float(input('Enter Amount :\t'))
    ac1.deposit(damount)

elif (choice==2):
    damount=float(input('Enter Amount :\t'))
    ac1.withdraw(damount)

elif (choice==3):
    ac1.show()

# else:
#     print('Wrong Choice')

#While example not complete
while choice<3:
    print('wrong choice')
    break


