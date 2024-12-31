# we all know why we use because of security purpose in case od pos data is floiwing freely and it is also not
# useful for real
#     world problem that is why we use oops

'''clas is define with the keyword class
class then classname and then colon
the object of the class can be variable function
or any thing
what the object need
Two thing
1 what the object have it is attributes
2 what it can do known as method
'''

# def function():
#     print(type('hello'))
# function()
''' that is why we say everything in python is a object
in this example what is in object "Hello" 
of which class called Str'''
# a=1
# def intiger():
#     print(type(a))
# intiger()
'''in this example what is in object "a" 
of which class called Int'''


# class FullName:
#     pass
# FullName_1=FullName()
# FullName_1.name="Muhammad Bilal"
# FullName_2=FullName()
# FullName_2.name='Muhammad Abdullah'
# print(FullName_1.name,'\n',FullName_2.name)



# class Instructor():
#     def __init__(self,inst_name,address):
#         self.name=inst_name
#         self.address=address
# instructor_1=Instructor('Abdullah','Quetta')
# print(instructor_1.name,instructor_1.address)
# instructor_2=Instructor('Bilal','Quetta')
# print(instructor_2.name,instructor_2.address)

'''Self is a keyword that bind the object attributes to the argument received'''
#
# class Instructor():
#     follower=0
#     # it is run for every object that we will create
#     def __init__(self,name,address):
#         self.name =name
#         self.address =address
#     def follower_count(self,follower_name):
#         self.follower += 1
#
# instructor_1=Instructor("Muhammad Abdullh","Quetta")
# print(instructor_1.name,instructor_1.address)
# instructor_1.follower_count('kamil')
# print(instructor_1.follower)
# instructor_2=Instructor("Kamil Jaffar","karachi")
# print(instructor_2.name,instructor_2.address)
# instructor_2.follower_count('abdullah')
# print(instructor_2.follower)


class Circle():
    pi=3.1416 #Class object attribute
    def __init__(self,radius):
        self.radius=radius
    def area_of_circle(self):
        area=self.pi*self.radius**2
        return area
    def get_circumference(self):
        return 2* self.pi *self.radius

area1=Circle(4)
print('"For calculating the area of the circle we need radius"\n "the radius of this circle is"',area1.radius)
print('The area of a circle is',area1.area_of_circle())
print('The circumference of a circle is',area1.get_circumference())



'''Finding the area of a rectangle'''
class Rectangle():
    def __init__(self,l,w):
        length=self.l
        self.w=w
        # self.area=l*w
    def get_area(self):
        area=self.l*self.w
        return area
rect1=Rectangle(4,7)
print(f'The area of the rectangle is {rect1.get_area()}')