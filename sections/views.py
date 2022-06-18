from django.shortcuts import render
from .forms import *
from django.contrib import messages
# Create your views here.
def addcoop12(request):
    form = Coop12Form(request.POST or None)
    if  form.is_valid():
        form.save()
        form = Coop12Form()
        messages.info(request,'บันทึกข้อมูลเรียบร้อยแล้ว') 
    context = {            
                'form' :form,           
    }
    return render(request,'test.html',context)