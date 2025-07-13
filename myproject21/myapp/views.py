from django.shortcuts import render
from django.http import HttpResponse 
from .models import EmployeeModel
from .models import FacultyModel
from .models import StudentModel
from .forms import EmployeeForm
from .forms import FacultyForm
from .forms import StudentForm
from django.template import loader
#display form & save data  typed in form
def display_home(request):
    return render(request, "master.html")  
    
def insert_faculty(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = FacultyForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_faculty.html", context)  
#view employee data
def view_faculty(request):
    ob=FacultyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_faculty.html')
    return HttpResponse(temp.render(context,request))
def view_faculty_delete(request):
    ob=FacultyModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_faculty_delete.html')
    return HttpResponse(temp.render(context,request))
def delete_faculty(request,pk):
    FacultyModel.objects.get(id=pk).delete()
    return render(request,"delete_faculty.html")
def update_faculty(request, pk):
    obj = FacultyModel.objects.get(id=pk)
    form = FacultyForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return render(request, "update_success.html")
    return render(request, "update_faculty.html", {'form': form})
def insert_student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)  
#view employee data
def view_student(request):
    ob=StudentModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_student.html')
    return HttpResponse(temp.render(context,request))

# View student data for deletion
def view_student_delete(request):
    ob = StudentModel.objects.all().values()
    context = {
        'data': ob
    }
    temp = loader.get_template('view_student_delete.html')
    return HttpResponse(temp.render(context, request))

# Delete student by ID
def delete_student(request, pk):
    StudentModel.objects.get(id=pk).delete()
    return render(request, "delete_student.html")

    # Update Student
def update_student(request, pk):
    obj = StudentModel.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return render(request, "update_success.html")
    return render(request, "update_student.html", {'form': form})


def insert_employee(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  
#view employee data
def view_employee(request):
    ob=EmployeeModel.objects.all().values()
    context={
        'data':ob
        }
    temp=loader.get_template('view_employee.html')
    return HttpResponse(temp.render(context,request))
 
# View employee data with delete option
def view_employee_delete(request):
    ob = EmployeeModel.objects.all().values()
    context = {
        'data': ob
    }
    temp = loader.get_template('view_employee_delete.html')
    return HttpResponse(temp.render(context, request))

# Delete employee by ID
def delete_employee(request, pk):
    EmployeeModel.objects.get(id=pk).delete()
    return render(request, "delete_employee.html")

    # Update Employee
def update_employee(request, pk):
    obj = EmployeeModel.objects.get(id=pk)
    form = EmployeeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return render(request, "update_success.html")
    return render(request, "update_employee.html", {'form': form})
