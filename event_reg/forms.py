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
    CHOICES = [('1', 'Married'), ('2', 'Un-Married')]
    CHOICES1 = [('M','Male'),('F','Female')]
    
    state_choices= [
    ('Andhra_Pradesh', 'Andhra Pradesh'),
    ]

    # event_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Write your name here'}))
    event_sub_category=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Write your name here'}))
    gender=forms.ChoiceField(choices=CHOICES1,widget=forms.Select(attrs={"class":"form-control",'placeholder': 'Choose your gender details'}))
    age=forms.IntegerField(min_value=1,max_value=99,widget=forms.NumberInput(attrs={'size':'2',"class":"form-control",'placeholder': 'Enter your age'}))
    mobile=forms.IntegerField(min_value=1,max_value=10000000000,widget=forms.NumberInput(attrs={'size':'10',"class":"form-control",'placeholder': 'Enter your mobile number'}))
    alternamte_mobile=forms.IntegerField(min_value=1,max_value=10000000000,widget=forms.NumberInput(attrs={'size':'10',"class":"form-control",'placeholder': 'Enter your alt-mobile number'}))
    marital_status=forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={"class":"form-control",'placeholder': 'Choose your marital status'}))
    birthdate=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"datepicker",'placeholder': 'Enter your Birthdate'}))
    address=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control",'placeholder': 'Enter your address'}))
    city=forms.CharField(widget=forms.Select(attrs={"class":"form-control","name":"city" ,"id":"citySelect", "size":"1",'placeholder': 'Enter your city name'}))
    state=forms.CharField(widget=forms.Select(choices=state_choices,attrs={"class":"form-control",'placeholder': 'Enter your sate name','id':"countrySelect","size":"1" ,"onchange":"makeSubmenu(this.value)"}))
    pincode=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control",'placeholder': 'Enter your pincode'}))
    # photo=forms.ImageField()
    # videofile=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Write your name here'}))

    class Meta:
        model=user_reg
        fields=['event_sub_category','gender','age','mobile','alternamte_mobile','marital_status','birthdate','state','city','pincode','address']
			

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')

