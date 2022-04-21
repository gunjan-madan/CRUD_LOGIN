from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from django.template import loader
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def home(req):
    return getEmployeeInfo(req)

def getEmployeeInfo(request):
    emps= Employee.objects.all()
    names= Employee.objects.values_list('employeeName', flat=True)
    print(emps)
    return render(request,'employees/home.html',{'employees':emps, 'names':names})


def register(request):
    if(request.method=='POST'):
        form= EmployeeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/employees/home')
            # return render(request, 'home.html')
    else:
        form= EmployeeForm()
        return render(request, 'employees/register.html', {'form':form})

def edit(request):
    id= request.GET.get('data')
    emp= Employee.objects.get(employeeID=id)
    if(request.method=='POST'):
        form= EmployeeForm(request.POST)
        if(form.is_valid()):
            form= EmployeeForm(request.POST,instance=emp)
            form.save()
            return HttpResponseRedirect('/employees/home')
    else:     
        form= EmployeeForm(initial=model_to_dict(emp))
        return render(request, 'employees/register.html', {'form':form})


def deleteEmp(request):
    id= request.GET.get('data')
    emp= Employee.objects.filter(employeeID=id)
    emp.delete()
    return HttpResponseRedirect('/employees/home')