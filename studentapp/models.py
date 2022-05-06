from django.db import models



class course(models.Model):
    course_name = models.CharField(max_length=225)
    fee = models.IntegerField()
    
    def __str__(self):
        return self.course_name
    

# Create your models here.
class Studentdetails(models.Model):
    course=models.ForeignKey(course, on_delete=models.CASCADE, null=True)
    student_name=models.CharField( max_length=90)
    student_address=models.TextField()
    student_dob=models.DateField()
    student_email=models.EmailField()
    student_phoneno=models.CharField(max_length=50)
    student_gender=models.CharField(max_length=50)
    student_qualification=models.CharField(max_length=50)
    # student_course=models.CharField(max_length=50)
    image = models.ImageField(default="defult2.jpg",upload_to="image/",blank=True,null=True)
    
    
    def __str__(self):
         return self.student_name
       
    

                                         