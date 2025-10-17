#parent class or base class or super class
class emp:
    def reg(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print('id:\t', self.id)
        print('name:\t', self.name)

    def welcome(self):
        print('Welcome')

#inherit class or derived class or child class
class dev(emp):
    def welcome(self):
        print('Welcome Developer')

d=dev()
d.welcome()
d.reg(1,'said')
d.display()

d=emp()
d.welcome()
d.reg(2,'siti')
d.display()