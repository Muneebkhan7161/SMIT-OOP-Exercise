class Person:
    def init(self, name, age):
        self.name = name  
        self.age = age    

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

class Student(Person):
    def init(self, name, age, grade):
        super().init(name, age)
        self.grade = grade  

    def introduce(self):
        print(f"Hi, I'm {self.name}, I'm {self.age} years old, and I'm in {self.grade} grade .")

person = Person("Muneeb", 26)
student = Student("Umar", 26, 12)

person.introduce()  
student.introduce()