from django.shortcuts import render,HttpResponse
from .models import employee,role,department
from datetime import datetime

def index(request):
    return render(request,'emp_app/index.html')

def all_emp(request):
    emps = employee.objects.all()
    context ={
        'emps': emps
    }
    print(context)
    return render(request,'emp_app/view_all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        last_name =request.POST.get('last_name')
        dept = request.POST.get('dept')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        
        
        if not all([first_name, last_name, salary, bonus, phone, dept, role]):
                return render(request, 'emp_app/add_emp.html', {'error': 'All fields are required.'})

        try:
            salary = int(salary) if salary else None
            bonus = int(bonus) if bonus else None
            phone = int(phone) if phone else None
            dept = int(dept)  if dept else None
            role = int(role) if role else None
        except ValueError:
            return render(request, 'emp_app/add_emp.html', {'error': 'Invalid input for salary, bonus, phone, dept, or role.'})
 
        new_emp = employee(first_name=first_name, last_name=last_name, salary =salary, bonus=bonus, phone=phone, dept_id =dept, role_id =role , hire_date =datetime.now()) 
        new_emp.save()
        
        return HttpResponse('Employee added successfully')
    
    elif request.method =='GET':   
      return render(request,'emp_app/add_emp.html')
  
    else:
        return HttpResponse('an Exception Occured! Employee Has Not Been Added')



def remove_emp(request):
    return render(request,'emp_app/remove_app.html')


def filter_emp(request):
    return render(request,'emp_app/filter_emp.html')

