from django.shortcuts import render
from .models import Establishment
from .filters import EstablishmentsFilter
from .forms import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse
from .resources import EstablishmentResource
from tablib import Dataset
# Create your views here.
def listestablishment(request):
    user_list = Establishment.objects.all()
    user_filter = EstablishmentsFilter(request.GET, queryset=user_list)
    return render(request, 'establishment/list.html', {'filter': user_filter})

def addestablishment(request):
    form = AddEstabForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = AddEstabForm()
        messages.info(request,'บันทึกข้อมูลเรียบร้อยแล้ว')
    context = {            
                'form' :form,           
    }
    return render(request,'establishment/addestablishment.html',context)

class UpdatePostView(UpdateView):
    model =  Establishment
    template_name = 'establishment/edit.html'
    fields =  '__all__'
    success_url= '/establishment/list'

class DeletePostView(DeleteView):
    model =  Establishment
    template_name = 'establishment/edit.html'
    fields =  '__all__'
    success_url= '/establishment/list'    

def export_establishment(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        employee_resource = EstablishmentResource()
        dataset = employee_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="establishments.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="establishments.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="establishments.xls"'
            return response   

    return render(request, 'establishment/export.html')

def import_establishment(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = EstablishmentResource()
        dataset = Dataset()
        new_employees = request.FILES['importData']

        if file_format == 'CSV':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='csv')
            result = employee_resource.import_data(dataset, dry_run=True)                                                                 
        
        elif file_format == 'JSON':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='json')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)

        elif file_format == 'XLS':
            imported_data = dataset.load(new_employees.read().decode('utf-8'),format='xls')
            # Testing data import
            result = employee_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            # Import now
            employee_resource.import_data(dataset, dry_run=False)

    return render(request, 'establishment/import.html') 
   