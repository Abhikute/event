from django.db import models
from django.conf import settings

from django.utils import timezone
# Create your models here.
from datetime import datetime



CATEGORY_CHOICES = (
    ('Shayari','Shayari'),
    ('Dance', 'Dance'),
    ('Music','Music'),
    ('Singing','Singing'),
    ('Photography','Photography'),
    ('Tiktok','Tiktok')
)
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )




class event(models.Model):
    event_name=models.CharField(max_length=125)
    event_photo=models.ImageField(upload_to="images/",null=True,blank=True)
    event_location=models.CharField(max_length=100)
    event_category=models.CharField(max_length=100,null=True,choices=CATEGORY_CHOICES, default='None')
    event_start_date=models.DateField(auto_now=False, auto_now_add=False)
    event_end_date=models.DateField(auto_now=False, auto_now_add=False)
    event_discription=models.TextField(blank=True,null=True)
    event_address=models.TextField(blank=True,null=True)
    event_instructuions=models.TextField(blank=True,null=True)
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




class user_reg(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    event=models.ForeignKey(event,on_delete=models.CASCADE, null=True, default=None)
    event_sub_category=models.CharField(max_length=80,null=True,blank=True)
    first_name=models.CharField(max_length=125,null=True,blank=True)
    Last_name=models.CharField(max_length=125,null=True,blank=True)
    Email=models.EmailField(max_length=254,null=True,blank=True)
    gender = models.CharField(max_length=1,null=True,blank=True, choices=GENDER_CHOICES)
    age=models.IntegerField(null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    alternamte_mobile=models.IntegerField(null=True,blank=True)
    marital_status=models.CharField(max_length=1,null=True,blank=True)
    birthdate=models.CharField(max_length=100,null=True,blank=True)
    address=models.TextField(blank=True,null=True)
    city=models.CharField(max_length=50,null=True,blank=True)
    state=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    id_proof=models.CharField(max_length=50,null=True,blank=True)
    identity_proof=models.ImageField(upload_to="images/",verbose_name='identity_proof',null=True,blank=True)
   
  
class PaytmHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_payment_paytm', on_delete=models.CASCADE, null=True, default=None)
    # user_reg = models.ForeignKey(user_reg, on_delete=models.CASCADE, default=None)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
    TXNID = models.CharField('TXN ID', max_length=64)
    BANKTXNID = models.IntegerField('BANK TXN ID', null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE')
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=40)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    STATUS = models.CharField('STATUS', max_length=12)
    user_reg=models.ForeignKey(user_reg,on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        app_label = 'event_reg'
        unique_together = (("ORDERID", "TXNID"),)

    def __unicode__(self):
        return self.STATUS
class Images(models.Model):
    user_reg = models.ForeignKey(user_reg, on_delete=models.CASCADE, default=None)
    event=models.ForeignKey(event,on_delete=models.CASCADE, null=True, default=None)
    image = models.ImageField(upload_to="images/",
                              verbose_name='Image')

class Temp_Images(models.Model):
    user_reg_id = models.IntegerField()
    image = models.ImageField(upload_to="temp_images/",
                              verbose_name='Image')

class Videos(models.Model):
    user_reg = models.ForeignKey(user_reg,on_delete=models.CASCADE, default=None)
    event=models.ForeignKey(event,on_delete=models.CASCADE, null=True, default=None)
    video=models.FileField(upload_to='videos/', null=True,blank=True, verbose_name="Videos")



class Temp_Videos(models.Model):
    user_reg_id = models.IntegerField() 
    video = models.ImageField(upload_to="temp_videos/",
                              verbose_name='Image')

   



