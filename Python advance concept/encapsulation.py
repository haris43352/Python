'''ENCAPSULATION MEAN RAPPED AOMETHING OR BUNDLED SOMETHING
OR WE CAN SAY THAT HIDE SOMETHING WITH THE HELP OF ACCESS SPECIFIER
OR WE WILL USE GETTER AND SETTER METHOD TO EXCESS PRIVATE METHOD OR VARIABLE


remember one thing is that abstraction  mean which thing are to be shown
 to the user works on design level or encapsulation work on implement level
 with the help of access specifier  hiding something these all concept are related to each other'''

class Employee:
    def __init__(self,name,age,department):
        self.name=name   # This is Public
        self._age=age    # This is Protected
        self.__department= department # This is private
    def get(self):
        return self.__department
    def set(self,department):
        self.__department=department
    def __work(self):
        print(f'I am working in {self.__department} department.')
    def display(self):
        self.__work()   # or we can use protected variable in the domain of class with the help of this also
        print(f'my name is {self.name} and my age is {self._age} and i am working in a company name HealthTec and in a {self.__department} department')


emp1=Employee("Abdullah",26,'Finance')
print(emp1.get())
print(emp1.set('Admin'))
