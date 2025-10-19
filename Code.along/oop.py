# Oop fundamentals
class student:
    def __init__ (self, name, type_of_studies, school, age, passed):
        # Attributes
        self.name = name
        self.type_of_studies = type_of_studies
        self.school = school
        self.age = age
        self.passed = passed

    # Methods
    def study(self):
        print(f"{self.name} is studying {self.type_of_studies} at {self.school}")

student1 = student(
    name = "Zakaria",
    type_of_studies = "Data Engineering",
    school = "STI",
    age = 27,
    passed = True
)

print(f"{student1.name} is studying {student1.type_of_studies} and he is {student1.age} years olds!")


