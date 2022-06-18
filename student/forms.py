from django import forms
from .models import *

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
        'STUDENT_NO': 'รหัสนักศึกษา',
        'Prefix': 'คำนำหน้า',
        'NAME' : 'ชื่อ',
        'LNAME':'สกุล ',
        'train_year':'ปีการศึกษา',
        'train_term':'เทอม ',
        'Faculty_name':'คณะ ',
        'Filed_study':'สาขา ',
        'train_room':'ห้อง ',
        

    }