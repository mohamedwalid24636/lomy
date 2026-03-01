from django.contrib import admin
from .models import User, InstructorProfile, StudentProfile, Category, Course, CourseContent, Enrollment, Review    

# Register your models here.


admin.site.register(User)
admin.site.register(InstructorProfile)
admin.site.register(StudentProfile) 
admin.site.register(Category)
admin.site.register(Course) 
admin.site.register(CourseContent)
admin.site.register(Enrollment)
admin.site.register(Review)
