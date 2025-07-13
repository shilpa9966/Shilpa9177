from django.urls import path
from . import views
urlpatterns = [
   path('',views.display_home,name='display_home'),
   path('insert_faculty/',views.insert_faculty, name='insert_faculty'),
   path('view_faculty/', views.view_faculty,  name = 'view_faculty'),
   path('insert_student/',views.insert_student, name='insert_student'),
   path('view_student/', views.view_student,  name = 'view_student'),
   path('update_faculty/<int:pk>/', views.update_faculty, name='update_faculty'),
   path('update_student/<int:pk>/', views.update_student, name='update_student'),
   path('view_faculty_delete/', views.view_faculty_delete,  name = 'view_faculty_delete'),
   path('delete_faculty/<int:pk>', views.delete_faculty,
           name = 'delete_faculty'),
   path('view_student_delete/', views.view_student_delete, name='view_student_delete'),
   path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),

   ]