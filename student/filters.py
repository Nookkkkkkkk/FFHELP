from .models import *
import django_filters

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['STUDENT_NO','NAME','LNAME','train_room', 'train_year', 'train_term', ]
        