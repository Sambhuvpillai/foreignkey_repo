from django.contrib import admin

# Register your models here.
from studentapp.models import Studentdetails
from studentapp.models import course

# register model

admin.site.register(Studentdetails)
admin.site.register(course)

# @admin.register(Studentdetails)
# class StudentdetailsAdmin(admin.ModelAdmin):
#     list_display = ('id','course','student_name','student_dob','student_email','student_phoneno')


