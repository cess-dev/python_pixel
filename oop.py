# class Student:
#     name="Eric"
#     age=22
# # object
# student1=Student()
# print(f"Name of Student: {student1.name}")

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("Eric", 22)
student2=Student("Cherop", 19)

print(student1.name)
print(student2.name)

# inheritance
