
'''IN MULTILEVEL INHERITANCE
   THERE IS ONE PARENT CLASS AND THE OTHER IS CHILD CLASS that IS INHERITING FORM PARENT CLASS AND THEN WE MAKE
   ANOTHER CHILD THAT IS INHERITING FROM THE FIRST CHILD CLASS THAT CHILD CLASS IS THE PARENT CLASS OF NEWLY CREATED
   CHILD CLASS AND THE OTHER CONCEPT ARE SAME

   '''

class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print('I can work')
class Male(Human):
    def __init__(self,run):
        self.run=run

    def eat(self):
        print('I can eat')
class Boy(Male):
    def __init__(self,code,name,age,run):
        self.code=code
        Human.__init__(self,name,age)
        Male.__init__(self,run)

boy1=Boy("Yes","Muhammad Abdullah",26,"yes")
print(boy1.name)
print(boy1.code)
print(boy1.run)
boy1.work()
boy1.run


