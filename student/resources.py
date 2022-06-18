from lib2to3.pgen2.token import NAME
from .models import *
from import_export import resources, widgets, fields
from student.models import *


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student





