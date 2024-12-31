'''THE MAIN DIFFERENCE BETWEEN THE PROTECTED AND PRIVATE IS THAT IN PROTECTED WE CAN EXCESS PROTECTED VARIABLE AND METHOD OUTSIDE THE CLASS
BUT IN PRIVATE WE CANNOT EXCESS PRIVATE VARIABLE AND PRIVATE METHOD OUTSIDE THE CLASS
 IF WE WANT TO USE PRIVATE VARIABLE OUTSIDE THE CLASS THEN WE HAVE TO USE 'NAME MANGLING'
  OR WITH THE HELP OF MAKING ONE FUNCTION LIKE THIS'''

class Employee:
    def __init__(self,name,age,department):
        self.name=name   # This is Public
        self._age=age    # This is Protected
        self.__department= department # This is private
    def __work(self):
        print(f'I am working in {self.__department} department.')
    def display(self):
        self.__work()   # or we can use protected variable in the domain of class with the help of this also
        print(f'my name is {self.name} and my age is {self._age} and i am working in a company name HealthTec and in a {self.__department} department')
class Company(Employee):
    def __init__(self,company_name,name,age,department):
        self.company_name=company_name
        super().__init__(name,age,department)
    def work(self):
        print(f"I am working in company {self.company_name}.")
        super()._Employee__work()    #This is called method overriding with the help of name mangling
comp1=Company('Health Tec','Abdullah',26 ,'Finance')
comp1.display()
# print(comp1._age)

# print(comp1.age)

comp1.work()

# print(comp1._Employee__department)

#
# comp1.age=29
# print(comp1.age)