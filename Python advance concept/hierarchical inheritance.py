'''IN HIERARCHICAL INHERITANCE ''THERE IS ONE PARENT CLASS AND MORE THEN ONE CHILD CLASS
    THAT IS INHERITING FROM THE PARENT CLASS AND THE BOTH CHILD HAS NO EXCESS TO OTHER CHILD ATTRIBUTES AND FUNCTION
    BECAUSE IF YOU CREATE AN INSTANCE OF ONE CHILD CLASS IT IS INHERITING FORM PARENT CLASS OR ITS OWN ATTRIBUTES AND
    METHOD AND DO NOT HAVE THE ABILITY TO EXCESS OTHER CHILD ATTRIBUTES AND METHOD
    BECAUSE THERE IS NO CONNECTION  between them'''
class Human:
    print("Running constructor")
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print("I can eat")
    def work(self):
        print('I can work')
    def details(self):
        print(f'My name is {self.name},and my age is {self.age}')

class Male(Human):
    print("constructor is running")
    def __init__(self,location):
        self.location=location
        # super().__init__(name,age)

    def work(self):
        super().work()
        print('I can code')

class Female(Human):
    def swim(self):
        print("I can swim")


# female1=Female()
# female1.work()
# female1.swim()

male1=Male()
# male1.work()
# male1.eat()
print(male1.name)
male1.details()