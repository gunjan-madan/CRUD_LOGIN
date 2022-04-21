from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.forms.models import model_to_dict
from .models import Student
from .forms import StudentForm,SignupForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return getStudentInfo(request)
    else:
        return HttpResponseRedirect('/login/')

# def home(request):
#     template= loader.get_template('home.html')
#     return HttpResponse(template.render()) 

# def home(request):
#     return HttpResponse('Welcome students!')

def getStudentInfo(request):
    studs= Student.objects.all()
    names= Student.objects.values_list('studentName', flat=True)
    # studs= Student.objects.get(studentID=1)
    print(studs)
    # studs= Student.objects.filter(studentClass__startswith='1')
    
    return render(request,'home.html',{'students':studs, 'names':names})


def register(request):
    if(request.method=='POST'):
        form= StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/home')
            # return render(request, 'home.html')
    else:
        form= StudentForm()
        return render(request, 'StudentDetails.html', {'form':form})


def studentDetails(request):
    id= request.GET.get('data')
    student= Student.objects.get(studentID=id)
    if(request.method=='POST'):
        form= StudentForm(request.POST,instance=student)
        if(form.is_valid()):       
            form.save()
            return HttpResponseRedirect('/home')
    else:     
        form= StudentForm(initial=model_to_dict(student))
        return render(request, 'StudentDetails.html', {'form':form})

def signup(request):
    if(request.method=='POST'):
        form= SignupForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request,'User created Successfully!')
            return HttpResponseRedirect('/home')
    else:
        form= SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if(request.method=='POST'):
            fm= AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                userName= fm.cleaned_data['username']
                pwd= fm.cleaned_data['password']
                user= authenticate(username=userName,password= pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home')
                else:
                    print("sdfsd")
                    messages.error(request,'Please provide valid credentials')
            else:
                    print("sdfsd")
                    messages.error(request,'Please provide valid credentials')
        else:
            fm= AuthenticationForm()        

        return render(request,'login.html', {'form':fm})
    
def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect('/login/')