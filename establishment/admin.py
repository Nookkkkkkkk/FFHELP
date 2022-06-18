from django.contrib import admin
from establishment.models import Establishment
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Establishment)
class EstablishmentAdmin(ImportExportModelAdmin):
    pass
