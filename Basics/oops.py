class Test:
    x = 10

t1 = Test()
t2 = Test()

Test.x = 20;
t1.x = 30
print(Test.x, t1.x,t2.x)




# class Test:
#     x = 10

# t1 = Test()
# t2 = Test()
# t1.x = 20

# print(t1.x,Test.x)

# print(t2.x)




# class Student:
#     name = "AshokIT"

#     @classmethod
#     def change_name(cls,new_name):
#         cls.name = new_name

# s1 = Student()
# print(s1.name)
# s2 = Student()

# Student.change_name("AshokIT-DataScience")
# print(s1.name)
# print(s2.name)



# class Student:

#     name = "AshokIT"

#     @classmethod
#     def test_func(obj):
#         print(obj.name)

# Student.test_func()



# class Student:
#     # class variables
#     msg = "AshokIT"

#     def __init__(self,name):
#         self.name = name

# s1 = Student("Std1")
# print(s1.name, s1.msg)

# s2 = Student("Std2")
# print(s2.name,s2.msg)






# class Student:
#     def __init__(self,name,age,marks,grade):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         self.grade = grade

#     def display(self):
#         print(self.name,self.age,self.marks,self.grade)

# s1 = Student("Std1",20,90,"A")
# s1.display()





# instance variables
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s1 = Student("Std1",20)
# print(s1.name,s1.age)
# s2 = Student("Std2",22)
# print(s2.name,s2.age)






# class Student:
#     def __init__(self):
#         print("Constructor Called")

# s1 = Student()




# class Student:
#     pass

# s1 = Student()
# print(type(s1))