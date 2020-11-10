class Employee:
	
	num_of_emps = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = int(pay)
		self.email = first + "." + last + '@company.com'
		
		Employee.num_of_emps += 1
		
	def fullname(self):
		return "{} {}".format(self.first, self.last)
		
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
		
	def __str__(self):
		return "{} - {}".format(self.fullname(), self.email)
		
	def __add__(self,other):
		return self.pay + other.pay
		
	def __len__(self):
	#total number of characters and full name
		return len(self.fullname())
		


class Developer(Employee):
	raise_amount = 1.10
	
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang
	
class Manager(Employee):
	
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else: 
			self.employees = employees
			
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
			
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emps(self):
		for emp in self.employees:
			print(" * ", emp.fullname())
		
	
	
	
emp1 = Developer("Hannah","Swain","500", "Python")
emp2 = Developer("Fred","Lovik","500", "Java")
mgr1 = Manager("Sue", "Smith", "900", [emp1])

print(emp1 + emp2)

print(len(emp1))


