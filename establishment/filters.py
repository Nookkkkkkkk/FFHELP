from .models import *
import django_filters

class EstablishmentsFilter(django_filters.FilterSet):
    class Meta:
        model = Establishment
        fields = ['name','province' ]
        