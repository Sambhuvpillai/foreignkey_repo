from django.urls import path,include
from.import views

urlpatterns = [
    # path('',views.register,name='register'),
    path('student_details',views.student_details,name='student_details'),
    path('show_student',views.show_student,name='show_student'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletestudent/<int:pk>',views.deletestudent,name='deletestudent'),
    path('studdatas/<int:pk>',views.studdatas,name='studdatas'),
    path('add_course',views.add_course,name='add_course'),
    path('',views.student1,name='student1'),
]
