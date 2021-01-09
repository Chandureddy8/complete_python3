class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades

bob = Student(math = 90, history = 90, writing = 90)  # 270
moe = Student(math = 100, history = 90, writing = 80) # 270
joe = Student(math = 40, history = 45, writing = 50)

print(bob.grades)
print(moe.grades)

print(bob == moe)
print(moe == bob)
print(bob == joe)
print(moe == joe)

print(bob != joe)
print(joe != moe)

