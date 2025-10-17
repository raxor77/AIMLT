# class bird:
#     def fly(self):
#         print('bird can fly')

# class jet(bird):
#     def fly(self):
#         print('jet fly')

# b=bird()
# print('bird implement')
# b.fly()

# print('Jet Implement')
# j=jet()
# j.fly()

# print('using for loop')
# for obj in [bird(), jet()]:
#     obj.fly()

class emp:
    def reg(self):
        self.id=int(input('input ID:\t'))
        self.name=input('input name:\t')

    def display(self):
        print('ID :',self.id)
        print('Name :',self.name)

class dev(emp):
    def reg(self):
        super().reg()
        self.domain=('Enter Domain\t')

    def display(self):
        super().reg()
        print('Domain :\t',self.domain)

d1=emp()
d1.reg()
d1.display()

d2=dev()
d2.reg()
d2.display()