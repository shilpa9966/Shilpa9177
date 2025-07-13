from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student

# 🛠️ Temporary password storage (for demo purposes only)
TEMP_PASSWORD_STORAGE = {}

# ✅ Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                if user.is_active:
                    auth_login(request, user)
                    request.session['just_logged_in'] = True
                    return redirect('home')
                else:
                    messages.error(request, '❌ Account is inactive. Contact admin.')
            else:
                messages.error(request, '❌ Invalid password.')
        except User.DoesNotExist:
            messages.error(request, '❌ Username does not exist.')

    return render(request, 'login.html')

# ✅ Home View (requires login)
@login_required(login_url='login')
def home(request):
    if request.session.pop('just_logged_in', False):
        messages.success(request, '✅ Successfully Logged In!')
    return render(request, 'home.html')

# ✅ Change Password (requires login)
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '').strip()
        new_password = request.POST.get('new_password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, "❌ Old password is incorrect.")
        elif new_password != confirm_password:
            messages.error(request, "❌ New passwords do not match.")
        else:
            user.set_password(new_password)
            user.save()
            auth_logout(request)
            messages.success(request, "✅ Password changed successfully! Please log in again.")
            return redirect('login')

    return render(request, 'changepassword.html')

# ✅ Register New User
def newuser(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, "❌ Username already exists.")
        else:
            User.objects.create_user(username=username, password=password)
            TEMP_PASSWORD_STORAGE[username] = password
            messages.success(request, "✅ Registered successfully! Please login.")
            return redirect('login')

    return render(request, 'newuser.html')

# ✅ Logout
@login_required(login_url='login')
def logout_view(request):
    auth_logout(request)
    messages.success(request, '✅ Logout successful!')
    return redirect('login')

# ✅ Add Student
@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST.get('name'),
            regno=request.POST.get('regno'),
            college=request.POST.get('college'),
            mobile=request.POST.get('mobile'),
            email=request.POST.get('email')
        )
        messages.success(request, "✅ Student added successfully!")
        return redirect('view_students')
    return render(request, 'add_student.html')

# ✅ View Students
@login_required(login_url='login')
def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})

# ✅ Update Student
@login_required(login_url='login')
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.regno = request.POST.get('regno')
        student.college = request.POST.get('college')
        student.mobile = request.POST.get('mobile')
        student.email = request.POST.get('email')
        student.save()
        messages.success(request, "✅ Student updated successfully!")
        return redirect('view_students')
    return render(request, 'update_student.html', {'student': student})

# ✅ Delete Student
@login_required(login_url='login')
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "✅ Student deleted successfully!")
        return redirect('view_students')
    return render(request, 'delete_student.html', {'student': student})

# ✅ Print Students
@login_required(login_url='login')
def print_students(request):
    students = Student.objects.all()
    return render(request, 'print_students.html', {'students': students})

# ✅ Forget Password (Demo)
def forget_password(request):
    password = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        if username in TEMP_PASSWORD_STORAGE:
            password = TEMP_PASSWORD_STORAGE[username]
            messages.success(request, f"✅ Password retrieved for {username}.")
        else:
            messages.error(request, "❌ Username not found or password unavailable.")
    return render(request, 'forgetpassword.html', {'password': password})
