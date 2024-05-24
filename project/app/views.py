from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile') 

        employee = Employee.objects.create(name=name,email=email,mobile=mobile)
        employee.save()

    # emp = Employee.objects.filter(name='Tejas Patil')
    emp = Employee.objects.all()
    return render(request,'home.html',{'emp':emp})

