from django.contrib import admin
from .models import FacultyModel
from .models import StudentModel
admin.site.register(FacultyModel)
admin.site.register(StudentModel)