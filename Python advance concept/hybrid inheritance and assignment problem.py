'''using Hybrid inheritance  we have  to solve one problem
hybrid inheritance is the mixture of different types of inheritance'''


class University:
    def __init__(self,uni_name):
        self.uni_name=uni_name
    def show_detail(self):
        print(f'The name of the university is {self.uni_name}.')

class Course(University):
    def __init__(self,course_name):
        self.course_name= course_name
    def show_detail(self):
        print(f'The name of the course is {self.course_name} .')

class Branch(University):
    def __init__(self, branch_name):
        self.branch_name=branch_name
    def show_detail(self):
        print(f"The name of the branch is {self.branch_name} .")

class Faculty(Branch):
    def __init__(self, faculty_name, branch_name, uni_name):
        self.faculty_name= faculty_name
        Branch.__init__(self,branch_name)
        University.__init__(self,uni_name)
    def show_detail(self):
        print(f'The name of the university is {self.uni_name}\n The name of the faculty is {self.faculty_name}\n The name of the branch is {self.branch_name}')

class Student(Course,Branch):
    def __init__(self, student_name, course_name, branch_name, uni_name):
        self.student_name = student_name
        Course.__init__(self, course_name)
        Branch.__init__(self, branch_name)
        University.__init__(self, uni_name)
    def show_detail(self):
        print(f'The name of the student is {self.student_name}\n The name of the Course is {self.course_name}\n The name of the branch is {self.branch_name}')


student1=Student("Muhammad Abdullah",'Engineering','Electronics','NED university of Engineering And Technology')
print(student1.branch_name)
print(student1.student_name)
print(student1.uni_name)
student1.show_detail()
student1.sh
faculty1 = Faculty('ECE','Electronics Engineering','NED university of Engineering And Technology')
faculty1.show_detail()
print(Student.mro())