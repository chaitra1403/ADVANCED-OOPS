def checkFun(value=False):
    if value==True:
        keys = ['emp_id','emp_name','emp_addr','status','desig','email']
    else:
        keys = ['comp_id','comp_name','comp_addr']

    def init(self,**kwargs):
        self.expected_keys = set(keys)
        if self.expected_keys != set(kwargs.keys()):
            raise ValueError("values not found")
        else:
            for k,v in kwargs.items():
                setattr(self,k,v)

    def empFun(self,*args,**kwargs):
        print("*"*10)
        print("employee details")
        self.pay=int(input("enter the pay:"))
        print("salary=",self.pay)
    
    def compFun(self,*args,**kwargs):
        print("*"*10)
        print("company details")
        self.noe=int(input("enter number of emp:"))
        self.nop=int(input("enter the no of proj:"))
        print("noe=",self.noe)
        print("nop=",self.nop)

    if value==True:
        return type('emp',(object,),{
            '__doc__':'employee details',
            '__init__':init,
            'empFun':empFun,
        })
    else:
        return type('comp',(object,),{
            '__doc__':'company details',
            '__init__':init,
            'compFun':compFun,
        })

emp =checkFun(True)
e1= emp(emp_id='employee1',emp_name='Chaitra',emp_addr='bangalore',status='on role',desig='developer',email='chaitra@gmail.com')
print(e1.__doc__)
print(e1.emp_id,'\n',e1.emp_name,'\n',e1.emp_addr,'\n',e1.status,'\n',e1.desig,'\n',e1.email)
e1.empFun()
comp= checkFun(False)
c1= comp(comp_id='company1',comp_name='google',comp_addr='bangalore')
print(c1.__doc__)
print(c1.comp_id,'\n',c1.comp_name,'\n',c1.comp_addr)
c1.compFun()
