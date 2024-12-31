'''inheritance mean inherit the attribute or method of the parent class
the main purpose of inheritance is that it will increase the reusability of the code'''

# class Human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     pass
"""here we notice one thing is that we only define function in parent class and we do not need to define this in child class 
so we are able to excess all the method of the super clas ya parent class"""
# Male_1=Male()
# Male_1.eat()

# class Human:# in this case we are defining some attributes in the parent class
#     def __init__(self):
#         self.eyes=2
#         self.nose=1
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     pass
# Male_1=Male()
# Male_1.eyes()
"""Here we notice we can also excess its attributes as well as method 
"""


# class Human:
#     def __init__(self):
#         self.eyes=2
#         self.nose=1
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def __init__(self,name):
#         self.name=name
#         super().__init__()
"""here notice one thing is that we have define a constructor of the child class write know we can not excess the a
attributes as well as its method as we are excessing previously here we have to define a super function to do this
 or while calling male object we have to give name because we have given name as its attribute"""
# Male_1=Male



# class Human:# if we define something in its constructor
#     def __init__(self,heart):
#         self.eyes=2
#         self.nose=1
#         self.heart=heart
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("I can work")
# class Male(Human):
#     def __init__(self,name,heart):#then we have to define heart here as well
#         self.name=name
#         super().__init__(heart)# also here as well
# male_1=Male("Abdullah",1)# or here als0
# male_1.eat()
# male_1.work()
# print(male_1.name)
# print(male_1.heart)


# class Human:
#         self.nose=nose# yha pa mna value define nai ki ha isi vja sa jub super or chilc class ma attribute name dena hoga
#         self.eyes=eyes
#         self.heart=heart
#     def eat(self):
#         print('I can eat')
#     def work(self):
#         print('I can work')
# class male(Human):
#     def __init__(self,name,heart,nose,eyes): #'when we define the init function of a child class then you won't be able to excess the attribute of the class so you haveto use super __init function to excess this
#       self.name=name
#       super().__init__(heart,nose,eyes) # why we define heart here because with the help of super we can excess the attributes of parent class that is why it is mandatory
#
#     def run(self):   # we can also define the method for each class like a child has properties then its parents
#         print('I can run')
#     def work(self):             # this is called method overriding if i will excess the work method it will print i can code
#         super().work()          # if we want our base class or parent class work as well as with the child class work then we will use super().work()
#                                 # super function give you the excess of the attribute or method of parent class
#         print('I can code')
#     def display(self):
#         print(f'I am {self.name} and I have {self.heart} heart')
# male1=male('Abdullah',1,1,2)
# print(male1.eyes)# male1.display()


"""METHOD OVERRIDING
 DEF WORK(SELF):
 PRINT("i CAN CODE)
    or 
    if we want the parent class work method 
    then we have to use 
    super.work()
    in the work function"""


"""   Summary 
inheritence mean a child can inherit the properties of its parents class like attributes and method
as soon as you define a constructor in child class you wont be able to exces the method and attribute of the
parent class so you have to use supper().__init() function to excess the atribute as well as its method
as we have define the attribute of while fefining a costructor like this def__init(name) then we have to give this name to
child class constructor or super class or we have to give another parameter to object of the child class that is name"""