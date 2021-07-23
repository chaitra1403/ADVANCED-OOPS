import pymysql
con=pymysql.connect()
print("Database Connected")
class mydb:
	def insert(self,sno,name,address,empcode,age,mob,desi):
		self.sno=sno
		self.name=name
		self.address=address
		self.empcode=empcode
		self.age=age
		self.mob=mob
		self.desi=desi
		cur=con.cursor()
		cur.execute(''' insert into emp (sno,name,address,empcode,age,mob,desi)values(%d,'%s','%s','%s',%d,%s,'%s')'''%(int(sno),name,address,empcode,int(age),int(mob),desi))
		con.commit()
		print("inserted")
		
	def display(self):
		cur=con.cursor()
		cur.execute(''' select * from emp''')
		print(cur.fetchall())
	def delete(self,slno):
		self.slno=slno
		cur=con.cursor()
		val=cur.execute('''delete from emp where sno=%d'''%(int(sno)))
		con.commit()
		if(val==1):
			print("1 Record delected")
		else:
			print("no record deleted")
	def update(self,sno,name):
		self.sno=sno
		cur=con.cursor()
		val=cur.execute('''update emp set name='%s' where sno=%d'''%(name,int(sno)))
		con.commit()
		if(val==1):
			print("1 Record updated")
		else:
			print("no record updated")
	def search(self,sno):
		self.sno=sno
		cur=con.cursor()
		val=cur.execute('''select * from emp where sno=%d'''%(int(sno)))
		con.commit()
		if(val==1):
			print("Record found")
		else:
			print("no record found")

obj=mydb()		
while True:
	print("1.INSERT 2.DISPLAY 3.DELETE 4.UPDATE 5.SEARCH")
	ch=int(input("Enter the choice"))
	if ch==1:
		sno=int(input("Enter sno"))
		name=input("Enter the name")
		address=input("Enter the address")
		empcode=input("Enter the code")
		age=int(input("Enter the age"))
		mob=int(input("Enter the mobile no "))
		desi=input("Enter the desgination")
		obj.insert(sno,name,address,empcode,age,mob,desi)
	elif ch==2:
		obj.display()
	elif ch==3:
		sno=int(input("ENter the sno"))
		obj.delete(sno)
	elif ch==4:
		sno=int(input("Enter sno"))
		name=input("ENter name")
		obj.update(sno,name)
	elif ch==5:
		sno=int(input("ENter the sno"))
		obj.search(sno)
