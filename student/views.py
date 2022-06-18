from unicodedata import name
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .filters import StudentFilter
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from .resources import StudentResource
from tablib import Dataset

def liststudent(request):
    user_list = Student.objects.all()
    user_filter = StudentFilter(request.GET, queryset=user_list)
    return render(request, 'student/list.html', {'filter': user_filter})

def addstudent(request):
    form = AddStudentForm(request.POST or None)
    if  form.is_valid():
        form.save()
        form = AddStudentForm()
        messages.info(request,'บันทึกข้อมูลเรียบร้อยแล้ว') 
    context = {            
                'form' :form,           
    }
    return render(request,'student/addstudent.html',context)
    

class UpdatePostView(UpdateView):
    model =  Student
    template_name = 'student/edit.html'
    fields =  '__all__'
    success_url= '/student/list'    

class DeletePostView(DeleteView):
    model =  Student
    template_name = 'student/edit.html'
    fields =  '__all__'
    success_url= '/student/list'    



def export_student(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        employee_resource = StudentResource()
        dataset = employee_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   

    return render(request, 'student/export.html')

def import_student(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        employee_resource = StudentResource()
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

    return render(request, 'student/import.html') 


