def sum(a=10,b=10):
	return a+b
	
class metatype(type):
	def __new__(cls,name,base,dict):
		print("NEW")
		print(cls)
		print(name)
		print(base)
		dict['s1:sum']=sum()
		print(dict)
		return super(metatype,cls).__new__(cls,name,base,dict)
		
		
	def __init__(cls,name,base,dict):
		print("INIT")
		print(cls)
		print(name)
		print(base)
		print(dict)
		super(metatype,cls).__init__(name,base,dict)
		
class Mykls(object,metaclass=metatype):
	def foo(self,parm):
		print(parm)
	
object=Mykls()
object.foo("CHAITRA")
print(object)
