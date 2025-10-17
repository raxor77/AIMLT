class emp:
    def __init__(self,id,name,qual):
        self.id=id
        self.name=name
        self.qual=qual

    def disp(self):
        print('ID :\t\t',self.id)
        print('Name :\t\t',self.name)
        print('Qualification :\t',self.qual)

class Dev(emp):
    def __init__(self, id, name, qual, domain, project):
        super().__init__(id, name, qual)
        self.domain=domain
        self.project=project
    def disp(self):
        super().disp()
        print('Domain :\t',self.domain)
        print('Project :\t',self.project)


e1=emp(1,'Sam','MCA')
print('\nEmployee details:')
e1.disp()

e2=Dev(2,'Ravi','Mtech','eshopping','dot net' )
print('\nDeveloper details:')
e2.disp()
