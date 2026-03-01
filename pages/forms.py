from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Course , Contact

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ,'first_name' , 'last_name' , 'is_instructor']


class CourseForm(forms.ModelForm):
    class Meta:
        model= Course
        fields =['title', 'description','category','price','is_free','level' ,'image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }
