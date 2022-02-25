class Student:

    def __init__(self, name, age, grade, is_absent):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_absent = is_absent

    def top_student(self):
        if self.grade >= 9:
            return True
        else:
            return False
