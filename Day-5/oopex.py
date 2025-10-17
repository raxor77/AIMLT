# class Emp:     #class ClassName:
#     def display(dis):    #defination of class
#         print('Display of Employee Class')   #attribute method, constractor

# obj = Emp()   #ObjectName = ClassName()
# obj.display()  #objectName.MethodName()

# te=Emp()
# te.display()

# #result display as below
# #Display of Employee Class
# #Display of Employee Class

#--------------
#2nd eg

class emp:
    def reg(self, eid, ename):
        self.eid=eid
        self.ename=ename
    def display(self):
        print('Employee ID : ',self.eid)
        print('Employee Name : ',self.ename)

e1=emp()
e2=emp()
e3=emp()
e1.reg(2,'hamid')
e2.reg(12,'zaleha')
e3.reg(24,'hamzah')
print('First employee details :\t')
e1.display()
print('Second employee details :\t')
e2.display()
print('Third employee details :\t')
e3.display()