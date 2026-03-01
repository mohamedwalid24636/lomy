from .models import Course, InstructorProfile , StudentProfile, Enrollment, Category , Contact
from django.shortcuts import render , redirect , get_object_or_404 
from .forms import CreateUserForm , CourseForm ,ContactForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required   ## for login required decorator
from .decorators import unauthenticated_user , allowed_users
from django.contrib import messages


# Create your views here. 

def web1(request):
    return render(request,'pages/web1.html')


def base(request):
    return render(request,'base.html')


def android(request):
    return render(request,'pages/android.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been sent successfully! \n we will contact you soon.')
            return redirect('contact')  # redirect after successful form submission
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})





def course_details(request , course_id):  ## view to display course details
    course = get_object_or_404(Course, id=course_id)  ## get course from database
    instructors =  course.instructors.all() ## get instructor from database
    contents = course.contents.all().order_by('order')
    context = {
        'course': course,
        'instructors': instructors,
        'contents': contents,
    }
    return render(request, 'pages/course-details.html', context)  ## render the course details page with course and instructor data
   



def cyber1(request):
    return render(request,'pages/cyber1.html')

def cyber2(request):
    return render(request,'pages/cyber2.html')

def coursw(request):
    return render(request,'pages/flutter.html')


# def index(request):
#     courses = Course.objects.all()  ## get all courses from database
#     categories = Course.objects.values('category').distinct()  ## get all categories from database
#     context = {
#         'courses': courses,
#         'categories': categories,
#     }
#     return render(request,'pages/index.html', context)  ## render the index page with courses and categories



def index(request):                                                     ## view to display all courses and categories   
    selected_category = request.GET.get('category')                    
    
    courses = Course.objects.all()
    if selected_category:
        courses = courses.filter(category=selected_category)
    
    categories = Course.objects.values('category__id', 'category__name').distinct()
    
    context = {
        'courses': courses,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'pages/index.html', context)


@allowed_users(allowed_roles=['Admin'])  ## only admin can access this page
def java(request):
    return render(request,'pages/java.html')

@unauthenticated_user    ## if user is already logged in, redirect to home page
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)      ## authenticate the user

        if user is not None:   ## if user is authenticated
            login(request, user)
            return redirect('home')
        else:
            # Invalid login credentials
            return render(request, 'pages/login.html', {'error': 'Invalid username or password.'})
    return render(request,'pages/login.html')

def logoutuser(request):                                                   # logout the user
    logout(request)
    return redirect('home')

@login_required(login_url='login')                                       # if user is not logged in, redirect to login page
def profile(request):
    return render(request,'pages/profile.html' , {'user': request.user})  ## render the profile page with user data



#registration page
@unauthenticated_user
def reg(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request,'pages/reg.html' , {'form':form})








# @login_required
# @allowed_users(allowed_roles=['instructor'])  ## only instructor can access this page
# def add_course(request):        ## view to add course
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             course = form.save(commit=False)
#             instructor = InstructorProfile.objects.get(user=request.user)
#             course.instructor = instructor
#             course.save()
#             return redirect('profile')
#     else:
#         form = CourseForm()
#     return render(request, 'pages/add_course.html', {'form': form})




@login_required
@allowed_users(allowed_roles=['instructor'])  # Only instructors can add courses
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()  # Save the course first
            try:
                instructor_profile = InstructorProfile.objects.get(user=request.user)
            except InstructorProfile.DoesNotExist:
                # Create an instructor profile if it doesn't exist
                instructor_profile = InstructorProfile.objects.create(user=request.user)

            # Link the course to the instructor
            instructor_profile.course = course
            instructor_profile.save()

            return redirect('home')
    else:
        form = CourseForm()

    return render(request, 'pages/add_course.html', {'form': form})


@login_required
@allowed_users(allowed_roles=['Instructor'])  ## only instructor can access this page
def delete_course(request, course_id):      ## view to delete course
    course = Course.objects.get(id=course_id)
    instructor = InstructorProfile.objects.get(user=request.user)
    if course.instructor == instructor:
        course.delete()
        return redirect('profile')
    else:
        return render(request,'pages/error.html', {'error': 'Unauthorized'})