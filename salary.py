class salary :
    value=0
    def print_salary(self):
        print('salary:',self.value)
    def print_net_salary(self,rate_percentage):
        rate=self.value/rate_percentage
        print('net salary:',self.value-rate)

salary=salary()
salary.value= 1500
salary.print_salary()
salary.print_net_salary(10)

class Person:

    
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def print_info(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('-----------------')

p1 = Person('Ahmad', 24)
p2 = Person('Maria', 19)

p1.print_info()
p2.print_info()
