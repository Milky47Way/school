from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def str(self):
        return self.user.username


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Classroom(models.Model):
    number = models.CharField(max_length=20)

    def str(self):
        return self.number


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def str(self):
        return self.user.username


class Lesson(models.Model):
    DAY_CHOICES = (
        (1, 'Понеділок'),
        (2, 'Вівторок'),
        (3, 'Середа'),
        (4, 'Четвер'),
        (5, 'П’ятниця'),
    )

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAY_CHOICES)
    lesson_number = models.IntegerField()  # 1-8
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    classroom = models.ForeignKey(Classroom, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('group', 'day', 'lesson_number')

    def str(self):
        return f"{self.group} | {self.subject} | {self.day}-{self.lesson_number}"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    value = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def str(self):
        return f"{self.student} - {self.value}"

