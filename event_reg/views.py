from django.shortcuts import render,redirect 
from .forms import user_geristration_form,SignUpForm
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import event,user_reg,PaytmHistory
import json
from django.db.models import Q
from django.conf import settings
from django.utils.decorators import method_decorator
from . import Checksum
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def user_regi(request):
	return render(request,'user_registration.html')
@login_required
def home(request):
	even=event.objects.all()

	return render(request,'index.html',{"event":even})


def success(request): 
	return HttpResponse('Registration successful') 

def contact(request):
	return render(request,'contact.html')




def about_us(request):
	return render(request,'aboutus.html')


def events(request):
	all_events=event.objects.all()
	locations=[]
	categorys=[]
	for item in all_events:
		if item.event_location not in locations or item.event_category not in categorys:
			locations.append(item.event_location)
			categorys.append(item.event_category)

	if request.method=='POST':
		location=request.POST.get('city')
		category=request.POST.get('category')
		
		if location=="Select City" and category=="Select Category":
			even=event.objects.all()
			return render(request,'events.html',{"event":even,"locations":locations,"categorys":categorys})

			
		else:
			print (location)
			even=event.objects.filter(Q(event_location=str(location)) | Q(event_category=str(category)))
			return render(request,'events.html',{"event":even,"locations":locations,"categorys":categorys})
			

	even=event.objects.all()
	
	return render(request,'events.html',{"event":even,"locations":locations,"categorys":categorys})


def services(request):
	return render(request,'services.html')

def event_details(request,pk=None):
	if pk:
		even=event.objects.get(pk=pk)
		all_events=event.objects.all()
		location=[]
		for item in all_events:
			if [item.event_location,event.objects.filter(event_location=item.event_location).count()] not in location:
				location.append([item.event_location,event.objects.filter(event_location=item.event_location).count()])
			 
			 


		return render(request,'event-details.html',{"event":even,"all_events":all_events,"location":location})

	
	return render(request,'event-details.html')


def usersignup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			email_subject = 'Activate Your Account'
			message = render_to_string('activate_account.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			print("Uid",urlsafe_base64_encode(force_bytes(user.pk)),"Token:",account_activation_token.make_token(user))
			email = EmailMessage(email_subject, message, to=[to_email])
			email.send()
			note='We have sent you an email, please confirm your email address to complete registration'
			return render(request,'registration/response.html',{"note":note})
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
def account_activation_sent(request):
	return render(request, 'account_activation_sent.html')


def activate_account(request, uidb64, token):
	try:
		uid = force_bytes(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
		print(user)
		print ("aalo me ethe")
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		# print (user)
		note="Your account has been activate successfully"
		return render(request,'registration/response.html',{"note":note})
	else:
		return HttpResponse('Activation link is invalid!')


def login(request):
	return render(request,'registration/login.html')



@login_required
def payment(request):
	user = request.user
	settings.USER = user
	MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
	MERCHANT_ID = settings.PAYTM_MERCHANT_ID
	# REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
	CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL + request.user.username + '/'
	# Generating unique temporary ids
	order_id = Checksum.__id_generator__()

	bill_amount = 100
	if bill_amount:
		data_dict = {
			'MID': MERCHANT_ID,
			'ORDER_ID': order_id,
			'TXN_AMOUNT': bill_amount,
			'CUST_ID': user.email,
			'INDUSTRY_TYPE_ID': 'Retail',
			'WEBSITE': settings.PAYTM_WEBSITE,
			'CHANNEL_ID': 'WEB',
			'CALLBACK_URL': CALLBACK_URL,
		}
		param_dict = data_dict
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
		return render(request, "payment.html", {'paytmdict': param_dict, 'user': user})
	return HttpResponse("Bill Amount Could not find. ?bill_amount=10")

# @login_required
@csrf_exempt
def response(request, user_id):
	if request.method == "POST":
		MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
		data_dict = {}
		for key in request.POST:
			data_dict[key] = request.POST[key]
		if data_dict.get('CHECKSUMHASH', False):
			verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
		else:
			verify = False
		if verify:
			for key in request.POST:
				if key == "BANKTXNID" or key == "RESPCODE":
					if request.POST[key]:
						data_dict[key] = int(request.POST[key])
					else:
						data_dict[key] = 0
				elif key == "TXNAMOUNT":
					data_dict[key] = float(request.POST[key])
			
			# REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
			PaytmHistory.objects.create(user=User.objects.get(username=user_id), **data_dict)
			user=User.objects.get(username=user_id)
			print(user.email)
			user_update=user_reg.objects.get(Email=user.email)
			user_update.registration_status="completed"
			user_update.payment_status="Done"
			user_update.save()
			return render(request, "response.html", {"paytm": data_dict,"user":user_id})
		else:
			return HttpResponse("checksum verify failed")
	else:
		return HttpResponse("Method \"GET\" not allowed")

	return HttpResponse(status=200)


def register(request,pk=None):

	if request.method == 'POST':
		registration_form={}
		files={}
		# print(request.FILES['photo'])
		for key in request.POST:
		  registration_form[key] = request.POST[key]

		for key in request.FILES:
			files[key]=request.FILES[key]
        

		# event_id=request.POST.get('event_id')
		# event_name=request.POST.get('event_name')
		# event_category=request.POST.get('event_category')
		# event_sub_category=request.POST.get('event_sub_category')
		# user_id=request.POST.get('user_id')
		# Last_name=request.POST.get('last_name')
		# Email=request.POST.get('email')
		# gender=request.POST.get('gender')
		# age=request.POST.get('age')
		# mobile=request.POST.get('mobile')
		# alternamte_mobile=request.POST.get('alt_mobile')
		# marital_status=request.POST.get('marital')
		# birthdate=request.POST.get('dob')
		# address=request.POST.get('address')
		# city=request.POST.get('city')
		# state=request.POST.get('state')
		# pincode=request.POST.get('pincode')
		# photo=request.POST.get('image')
		# videofile=request.POST.get('videofile')
		registration_form.pop("csrfmiddlewaretoken", None)

		registration={**registration_form,**files}
		print(registration)
		print (files)
	
		user_reg.objects.create(**registration)

		user = request.user
		settings.USER = user
		MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
		MERCHANT_ID = settings.PAYTM_MERCHANT_ID
		# REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
		CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL + request.user.username + '/'
		# Generating unique temporary ids
		order_id = Checksum.__id_generator__()

		bill_amount = 100
		if bill_amount:
			data_dict = {
				'MID': MERCHANT_ID,
				'ORDER_ID': order_id,
				'TXN_AMOUNT': bill_amount,
				'CUST_ID': user.email,
				'INDUSTRY_TYPE_ID': 'Retail',
				'WEBSITE': settings.PAYTM_WEBSITE,
				'CHANNEL_ID': 'WEB',
				'CALLBACK_URL': CALLBACK_URL,
			}
			param_dict = data_dict
			param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
			return render(request, "payment.html", {'paytmdict': param_dict, 'user': user})
		return HttpResponse("Bill Amount Could not find. ?bill_amount=10")
		# registration_form.pop("csrfmiddlewaretoken", None)
		# print(event_id,event_name,event_category,event_sub_category,first_name,Last_name,Email,gender,age,mobile,alternamte_mobile,marital_status,birthdate,address,city,state,pincode,photo,videofile)
	
	if pk:
		even=event.objects.get(pk=pk)
		try:
			reg_user=user_reg.objects.get(Email=request.user.email)
			print (reg_user.Email)
		except:
			reg_user=None
			pass
		form=user_geristration_form()

		return render(request,'Register-now.html',{"event":even,"form":form,"reg_user":reg_user})


	form=user_geristration_form()
	return render(request,'Register-now.html',{"form":form})