from pyexpat import model
from django.db import models
from student.models import Student
from establishment.models import Establishment
# Create your models here.

class Coop12(models.Model):
    score20 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
        ("15","15"),
        ("16","16"),
        ("17","17"),
        ("18","18"),
        ("19","19"),
        ("20","20"),
    )
    score10 = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
    )
    
    student = models.ManyToManyField(Student)
    establishment = models.ManyToManyField(Establishment)
    verse1 = models.CharField(max_length=255,choices=score20)
    verse2 = models.CharField(max_length=255,choices=score20)
    verse3 = models.CharField(max_length=255,choices=score10)
    verse4 = models.CharField(max_length=255,choices=score10)
    verse5 = models.CharField(max_length=255,choices=score10)
    verse6 = models.CharField(max_length=255,choices=score10)
    verse7 = models.CharField(max_length=255,choices=score10)
    verse8 = models.CharField(max_length=255,choices=score10)
    verse9 = models.CharField(max_length=255,choices=score10)
    verse10 = models.CharField(max_length=255,choices=score10)
    verse11 = models.CharField(max_length=255,choices=score10)
    verse12 = models.CharField(max_length=255,choices=score10)
    verse13 = models.CharField(max_length=255,choices=score10)
    verse14 = models.CharField(max_length=255,choices=score10)
    verse15 = models.CharField(max_length=255,choices=score10)
    verse16 = models.CharField(max_length=255,choices=score10)
    verse17 = models.CharField(max_length=255,choices=score10)
    verse18 = models.CharField(max_length=255,choices=score10)
    text = models.TextField(max_length=255)
