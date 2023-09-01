
class Student:

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def getInto(self):
        print("This is ",self.name, " and my marks are ",self.marks)


class StudentGradeCalculator:

    def gradeCalculator(self,student):

        if(student.marks >= 90 and student.marks <=100):
            return "Grade A"
        elif(student.marks >= 80 and student.marks <90):
            return "Grade B"
        elif (student.marks >= 70 and student.marks < 80):
            return "Grade C"
        else:
            return "Fail"


st1 = Student(111,"Rajesh",83)
gcalc = StudentGradeCalculator()
print(gcalc.gradeCalculator(st1))