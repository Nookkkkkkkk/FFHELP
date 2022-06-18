from django.db import models

# Create your models here.
class Student(models.Model):
    PREFIX_Students = (
        ("นาย","นาย"),
        ("นาง","นาง"),
        ("นางสาว","นางสาว"),
    )
    TERM = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
    )
    
    Faculty_of = (
        ("วิศวกรรมศาสตร์","วิศวกรรมศาสตร์"),
    )

    STUDY_name = (
        ("คอมพิวเตอร์","คอมพิวเตอร์"),
    )   
    ROOM = (
        ("ECP1N","ECP1N"),
        ("ECP2N","ECP2N"),
        ("ECP3N","ECP3N"),
        ("ECP4N","ECP4N"),
        ("ECP2R","ECP2R"),
        ("ECP3R","ECP3R"),
        ("ECP4R","ECP4R"),
        ("ECP2Q","ECP2Q"),
        ("ECP3Q","ECP3Q"),
        ("ECP4Q","ECP4Q"),
        
    )
    STUDENT_NO = models.CharField(max_length=255,unique=True)
    Prefix = models.CharField(max_length=255,choices=PREFIX_Students)
    NAME = models.CharField(max_length=255)
    LNAME = models.CharField(max_length=255)
    train_year = models.CharField(max_length=255,)
    train_term  = models.CharField(max_length=255,choices=TERM)
    Faculty_name = models.CharField(max_length=255,choices=Faculty_of,default='วิศวกรรมศาสตร์')
    Filed_study = models.CharField(max_length=255,choices=STUDY_name,default='คอมพิวเตอร์')
    train_room = models.CharField(max_length=255,choices=ROOM)
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.STUDENT_NO+" ชื่อ-สกุล: "+self.Prefix+" "+self.NAME+" "+self.LNAME+" ปีการศึกษา: "+self.train_year+" เทอม: "+self.train_term+" คณะ: "+self.Faculty_name+" สาขา: "+self.Filed_study+" ห้อง: "+self.train_room