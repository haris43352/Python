'''POLY MEAN MANY AND MORPHISM MEAN FORMS
LIKE WE BEHAVE DIFFERENTLY IN DIFFERENT SITUATION THE TYPES OF POLYMORPHISM
IS UNDER BELOW
DUCK TYPING
METHOD OVERRIDING
METHOD OVERLOADING
OPERATOR OVERLOADING
'''
# FIRSTLY DISCUSSING DUCK TYPING
'''IN DUCK TYPING WE DO NOT CARE ABOUT THE CLASS OBJECT IN ORDER TO CALL
 EXISTING METHOD ON THE OBJECT IF THAT METHOD OR ATTRIBUTE IS DEFINE ON THAT OBJECT 
 IT WILL BE CALLED 
 >CLASS DOES NOT MATTER 
 >PYTHON HAS DYNAMIC TYPE OF WRITING '''

class Duck:
    def swim(self):
        print('Swim')
    def speak(self):
        print('Quack Quack')
class Dog:
    def swim(self):
        print('swim')
    def speak(self):
        print('Wao Wao')
def display(obj):
    # print()
    obj.swim()
    obj.speak()
duck=Duck()
display(duck)