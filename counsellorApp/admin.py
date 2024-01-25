from django.contrib import admin
from .models import ClassTable,StudentTable

# Register your models here.
admin.site.register(ClassTable)
admin.site.register(StudentTable)