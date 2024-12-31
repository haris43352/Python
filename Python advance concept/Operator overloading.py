# class Complexnumber:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i
#     def __add__(self, other):
#        # return f'{self.r+ other.r} +{ self.i + other.i}i'
#          return str(self.r+other.r)+  '+' + str(self.i+other.i) + "i"
# c1=Complexnumber(2,3)
# c2=Complexnumber(3,4)
# print(c1+c2)

'''THIS IS CALLED METHOD OVERLOADING BECAUSE THIS IS NOT USING '''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False
p1=Person('Abdullah',26)
p2=Person('Bilal',24)

if p1>p2:
    print(f"Bill will be paid by {p1.name}")

else:
    print(f'Bill will be paid by {p2.name}')