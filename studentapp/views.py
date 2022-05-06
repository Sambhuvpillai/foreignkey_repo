import os
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
# def register(request):
#     return render(request, 'register.html')
# def course1(request):
#     return render(request, 'course.html')
def student_details(request):
    
    if request.method=='POST':
        sname=request.POST['student_name']
        add=request.POST['student_address']
        dob=request.POST['student_dob']
        gender=request.POST['student_gender']
        mail=request.POST['student_email']
        phone=request.POST['student_phoneno']
        qualification=request.POST['student_qualification']
        # course=request.POST['student_course']
        image=request.FILES.get('file')
        sel1=request.POST['sel']
        course1=course.objects.get(id=sel1)
        

        student=Studentdetails(student_name=sname,
                               student_address=add,
                               student_dob=dob,
                               student_gender=gender,
                               student_email=mail,
                               student_phoneno=phone,
                               student_qualification=qualification,
                            #    student_course=course,
                               image=image,
                               course=course1)
        student.save()
        # courses=course.objects.all()
        # context={'courses':courses}
    
        # return render(request, 'showstud.html',context)
        print("hii")
        return redirect('show_student')
    
    
def show_student(request):
    students=Studentdetails.objects.all()
    # students=course.objects.all()
    return render(request,'showstud.html',{'students':students})

def editpage(request,pk):
    students=Studentdetails.objects.get(id=pk)
    return render(request,'edit.html',{'student':students})

def edit_student_details(request,pk):
    if request.method=='POST':
        student=Studentdetails.objects.get(id=pk)
        student.student_name = request.POST.get('student_name')
        student.student_address = request.POST.get('student_address')
        student.student_dob = request.POST.get('student_dob')
        student.student_gender = request.POST.get('student_gender')
        student.student_email = request.POST.get('student_email')
        student.student_phoneno = request.POST.get('student_phoneno')
        student.student_qualification = request.POST.get('student_qualification')
        student.student_course = request.POST.get('student_course')
        
        student.save()
        return redirect('show_student')
    return render(request, 'edit.html',)

def deletestudent(request,pk):
    students=Studentdetails.objects.get(id=pk)
    if students.image is not None:
        if not students.image =="/static/image/defult2.jpg":
            os.remove(students.image.path)
        else:
            pass
    students.delete()
    # if len(students.image) > 0:
    #     os.remove(students.image.path)
    # students.delete()
    return redirect('show_student')

def studdatas(request,pk):
    students=Studentdetails.objects.get(id=pk)
    return render(request,'studentdetail.html',{'student':students})



# add course

def add_course(request):
    if request.method=='POST':
        cors=request.POST['course']
        cfee=request.POST['fee']
        print(cors)
        crs=course()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        print("hii")
        return redirect('student1')
    return render(request, 'course.html')
    
    
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    
    return render(request, 'register.html',context)
    
