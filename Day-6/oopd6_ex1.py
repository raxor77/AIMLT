# class player:
#     def __init__(self):
#         print('Welcome New Player')

#     def reg(self,id , name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f'ID: {self.id} \t Name: {self.name} \t Team: {self.team}')

# #object creation
# p1=player()
# p2=player()
# p3=player()
# p1.reg(1,'Abdul','Kelantan')
# p2.reg(2,'Daud','Johor')
# p3.reg(3,'Cek','Terengganu')

# p1.display()
# p1.display()
# p3.display()


#Parameterised constructor
class player:
    def __init__(self, id, name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f'ID: {self.id} \t Name: {self.name} \t Team: {self.team}')

    def __str__(self):
        return f'{self.id} {self.name} {self.team}'

#object creation
p1=player(1,'Abdul','Kelantan')
p2=player(2,'Daud','Johor')
p3=player(3,'Cek','Terengganu')

#Display player details
# player=int(input('Enter player ID:')) #<my test to call but fail
p1.display()
p2.display()
p3.display()

print(p1) #< need def str in 36, if no error