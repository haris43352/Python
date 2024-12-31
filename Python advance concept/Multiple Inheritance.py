class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
class Mercedes:
    def __init__(self,differentiating_from_other):
        self.differentiating_from_other= differentiating_from_other
    def feel_comfortable(self):
        print("The mercedes cars are very comfortable")
class Audi(Car,Mercedes):
    def __init__(self,logo,differentiating_from_other,name,model):
        self.logo=logo
        Mercedes.__init__(self,differentiating_from_other)
        Car.__init__(self,name,model)
    def modifying_name(self,updated_name):
        self.name=updated_name
'''Or one thing has to be remember here is that if you define your constructor then you have to define seperatily init function with the Class name
or if you do not define it will not work '''

audi1=Audi('4 Rings','the iconic German engineering','E tron','Base model')
print(audi1.name)
audi1.feel_comfortable()
print(audi1.model)
audi1.modifying_name('Etron Gt')
print(audi1.name)
# print(a)
''' FOR MODIFYING ATTRIBUTES VALUES WE CAN SIMPLY WRITE AN NSTANCE NAME '.' WITH VARIABLE WHICH YOU WANT TO MODIFy
                                         or
   YOU CAN DO WITH THE HELP OF METHOD THAT IS SHOWN ABOBE IN WHICH WE DEFINE A FUNCTION CALLED UPDATE_NAME THEN SETTING NAME VALUE TO THE UPDATED VALUE THEN CALLING FUNCTION WITH THE
   UPDATED NAME THEN AFTER WRITING AN INSTANCE NAME "." WITH VARIABLE NAME
'''



# class Human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print('I can work')
# class male:
#     def flirt(self):
#         print('I can flirt')
#     def cook(self):
#         print('I can cook')
#     def work(self):
#         print('I can code')
#
# class Boy(Human,male):
#     def sleep(self):
#         print('I can sleep')
#     def work(self):
#         print('I can tst')
# boy1=Boy()
# boy1.work()
# Human.work(boy1)    '''It is for the when we want to excess the specific work of class 1 which class then which func then where you want this'''
#



