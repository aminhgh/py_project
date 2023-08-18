#class - inheritance 
#class person

class person():
    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def person_info(self):
        print(self.name)
        print(self.last_name)
        print(self.age)

class student(person):
    def __init__(self,student_id,name,last_name,age):
        person.__init__(self,name,last_name,age)
        self.student_id = student_id

    def student_info(self):
        print(self.student_id)

student_1 = student(100066645,"amin","hgh",22)
#student_info
student_1.student_info()
#person_info
student_1.person_info()