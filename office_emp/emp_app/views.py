
from django.shortcuts import render,HttpResponse,redirect
from .models import Employee,Role,Department
from datetime import datetime
from django.urls import reverse
from .forms import EmployeeForm
from django.urls import reverse
from django.db.models import Q 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login,logout as auth_logout


def index(request):
    return render(request,'emp_app/index.html')


def all_emp(request):
    employees = Employee.objects.all()
    
    if request.method == "GET":
     query = request.GET.get('searchname','').strip()
     
    if query:
        words = query.split()
        employees = employees.filter(Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(role__name__icontains=query) |
            Q(dept__name__icontains=query))
        
        if len(words) == 2:
            employees |= Employee.objects.filter(
            Q(first_name__icontains=words[0]) & Q(last_name__icontains=words[1])
        )
            
    return render(request, 'emp_app/views_all_emp.html', {'employees': employees,'query': query})


def add_emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(reverse('emp_app:all_emp'))  

    else:
        form = EmployeeForm()

    departments = Department.objects.all()
    roles = Role.objects.all()
    
    return render(request, 'emp_app/add_emp.html', {'form': form, 'departments': departments, 'roles': roles})


def remove_emp(request):
    employees = Employee.objects.all()  
    if request.method == "POST":
        emp_ids = request.POST.getlist("emp_ids")  

        if emp_ids: 
            Employee.objects.filter(id__in=emp_ids).delete()
            return redirect(reverse('emp_app:all_emp'))  
        
        return render(request, "emp_app/remove_emp.html", {"employees": employees, "error": "No employee selected!"})

    return render(request, "emp_app/remove_emp.html", {"employees": employees})



# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             auth_login(request,new_user)
#             # return redirect('user:dashboard')
#         else:
#             return render(request,'emp_app/register.html',{'form': form})
       
#     else: 
#         form = UserCreationForm()
#         return render(request, 'emp_app/register.html', {'form': form})




# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request,data=request.POST)
#         if form.is_valid():
#             new_user = form.get_user()
#             auth_login(request,new_user)
#             # return redirect('user:dashboard') 
#         else:
#             return render(request,'emp_app/login.html',{'form':form})

#     form = AuthenticationForm()
#     return render(request,'emp_app/login.html',{'form': form})  
