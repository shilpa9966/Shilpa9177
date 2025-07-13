from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('newuser/', views.newuser, name='newuser'),
    path('changepassword/', views.change_password, name='change_password'),
    path('add_student/', views.add_student, name='add_student'),
    path('view_students/', views.view_students, name='view_students'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('print_students/', views.print_students, name='print_students'),
    path('forgetpassword/', views.forget_password, name='forgetpassword'),  # ← ADD COMMA HERE ✅
]
