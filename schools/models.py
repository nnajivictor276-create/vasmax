from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    pin = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.full_name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.IntegerField()
    def grade(self):
        if self.score >= 70: return "A"
        elif self.score >= 60: return "B"
        elif self.score >= 50: return "C"
        elif self.score >= 40: return "D"
        else: return "F"
    def __str__(self):
        return f"{self.student.full_name} - {self.subject} - {self.score}"