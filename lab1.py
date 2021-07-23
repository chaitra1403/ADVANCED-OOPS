import time

def calculate(func):
	def inner():
		start=time.time()
		f=func()
		end=time.time()
		print("Time taken is ",end-start)
		return f
	return inner



def fib():
		a,b=0,1
		while True:
			a,b=b,a+b
			yield a
			
@calculate
def take():			
	g=fib()
	n=int(input("ENter the number"))
	for i in range(n):
		print(next(g))

	#fib()

take()
