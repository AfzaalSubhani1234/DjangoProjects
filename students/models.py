
from django.db import models


class Course(models.Model):
    COURSE_CHOICES = [
        ("AI", "Artificial Intelligence"),
        ("PYTHON_FS", "Python Full Stack"),
        ("DJANGO", "Django"),
        ("DRF", "Django REST Framework"),
        ("FASTAPI", "FastAPI"),
        ("REACT", "React"),
        ("JS", "JavaScript"),
        ("DATA_SCIENCE", "Data Science"),
        ("ML", "Machine Learning"),
        ("DATABASE", "Database Management"),
    ]

    name = models.CharField(
        max_length=100,
        choices=COURSE_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="students"
    )

    def __str__(self):
        return self.name
