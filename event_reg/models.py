from django.db import models

# Create your models here.



CATEGORY_CHOICES = (
    ('Shayari','Shayari'),
    ('dance', 'Dance'),
    ('music','Music'),
    ('singing','Singing'),
    ('drama','Drama')
)
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )




class registrations(models.Model):
	# event_id=models.CharField(max_length=100,null=True,blank=True)
	# first_name=models.CharField(max_length=125,null=True)
	# Last_name=models.CharField(max_length=125,null=True)
	# Email=models.EmailField(max_length=254,null=True,blank=True)
	# gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	# age=models.IntegerField(null=True,blank=True)
	# mobile=models.IntegerField(null=True,blank=True)
	# alternamte_mobile=models.IntegerField(null=True,blank=True)
	# marital_status=models.CharField(max_length=1)
	# birthdate=models.DateField(null=True,blank=True)
	# address=models.TextField(blank=True,null=True)
	# city=models.CharField(max_length=50,null=True)
	# state=models.CharField(max_length=50,null=True)
	# pincode=models.IntegerField(null=True,blank=True)
	photo=models.ImageField(upload_to="images/",null=True,blank=True)
	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
    
class user_reg(models.Model):
	event_id=models.CharField(max_length=100,null=True,blank=True)
	event_category=models.CharField(max_length=80,null=True,blank=True)
	event_sub_category=models.CharField(max_length=80,null=True,blank=True)
	first_name=models.CharField(max_length=125,null=True)
	Last_name=models.CharField(max_length=125,null=True)
	Email=models.EmailField(max_length=254,null=True,blank=True)
	gender = models.CharField(max_length=1,null=True, choices=GENDER_CHOICES)
	age=models.IntegerField(null=True,blank=True)
	mobile=models.IntegerField(null=True,blank=True)
	alternamte_mobile=models.IntegerField(null=True,blank=True)
	marital_status=models.CharField(max_length=1,null=True)
	birthdate=models.DateField(null=True,blank=True)
	address=models.TextField(blank=True,null=True)
	city=models.CharField(max_length=50,null=True)
	state=models.CharField(max_length=50,null=True)
	pincode=models.IntegerField(null=True,blank=True)
	photo=models.ImageField(upload_to="images/",null=True,blank=True)
	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
	

class event(models.Model):
 	event_name=models.CharField(max_length=125)
 	event_photo=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_location=models.CharField(max_length=100)
 	event_category=models.CharField(max_length=100,null=True,choices=CATEGORY_CHOICES, default='None')
 	event_start_date=models.DateField(auto_now=False, auto_now_add=False)
 	event_end_date=models.DateField(auto_now=False, auto_now_add=False)
 	event_discription=models.TextField(blank=True,null=True)
 	event_address=models.TextField(blank=True,null=True)
 	event_highlight1=models.TextField(blank=True,null=True)
 	event_highlight2=models.TextField(blank=True,null=True)
 	event_highlight3=models.TextField(blank=True,null=True)
 	event_highlight4=models.TextField(blank=True,null=True)
 	event_highlight5=models.TextField(blank=True,null=True)
 	event_highlight6=models.TextField(blank=True,null=True)
 	event_photo1=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo2=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo3=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo4=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo5=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo6=models.ImageField(upload_to="images/",null=True,blank=True)
 	event_photo7=models.ImageField(upload_to="images/",null=True,blank=True)
