from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Custom User model
class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    user_img = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)




# Student profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_courses = models.ManyToManyField('Course', blank=True, related_name='favored_by')

# Category for courses
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_free = models.BooleanField(default=False)
    level = models.CharField(max_length=50, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.title

# Course content (videos/lessons)
class CourseContent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents' )
    title = models.CharField(max_length=200)    ####
    video_url = models.URLField(blank=True, null=True)  ###
    duration = models.DurationField(blank=True, null=True) ###
    video_file = models.FileField(upload_to='videos/', blank=True, null=True) ###
    order = models.PositiveIntegerField()
    details = models.TextField(blank=True) ###
    def __str__(self):
        return self.title


# Instructor profile
class InstructorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instructors' , null=True, blank=True)
    name = models.CharField(max_length=200 , null=True, blank=True)
    Instructor_image = models.ImageField(upload_to='instructor_images/', null=True, blank=True)
    bio = models.TextField(blank=True)
    rating = models.FloatField(default=0.0)
    social_links = models.TextField(blank=True)
    experience = models.IntegerField(blank=True , null=True)
    num_studenta = models.IntegerField(blank=True , null=True)
    def __str__(self):
        return self.name







# Enrollment model
class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.FloatField(default=0.0)

# Reviews and ratings
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Orders / Payments
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])
    payment_date = models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField(max_length=100  , null=True)
    email = models.EmailField(null=True)
    message = models.TextField( null=True)

    def __str__(self):
        return self.email