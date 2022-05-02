from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,"all_emp.html",context)

def add_emp(request):
            if request.method=='POST':
                first_name=request.POST.get("first_name")
                last_name=request.POST.get("last_name") 
                salary=int(request.POST.get("salary") )
                bonus=int(request.POST.get("bonus") )
                phone=int(request.POST.get("phone") )
                dept=request.POST.get("dept") 
                role=request.POST.get("role")
                hire_date=request.POST.get("hire_date") 
                new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
                new_emp.save()
                return HttpResponse('''<br><br><center><h3>congratulation Employee added successfully<br><a style="" href="/add_emp">Back</a></h3></center>''')
            elif request.method=="GET": 
                return render(request,"add_emp.html")
            else:
                return HttpResponse('''<br><br><center><h5>An Exceptoion occured! Employee <a href="/add_emp">Back</a></h5></center>''')
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('''<br><br><center><h3>congratulation Employee Removed successfully <br><a style="" href="/remove_emp">Back</a></h3></center>''')
  

        except:
            return HttpResponse("<br><br><center><h3>please enter Valid! Employee</h3></center>")

    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,"remove_emp.html",context)

def filter_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,"filter_emp.html",context)