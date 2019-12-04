from django import forms
from .models import user_reg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female'),
    ('other','Other'),

)

class user_geristration_form(forms.ModelForm):
	class Meta:
		model=user_reg
		fields=['photo','videofile']
			

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

