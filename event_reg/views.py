from django.shortcuts import render,redirect 
from .forms import user_geristration_form,SignUpForm
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import event,user_reg,PaytmHistory,Images,Videos
import json
from django.db.models import Q
from django.conf import settings
from django.utils.decorators import method_decorator
from . import Checksum
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def home(request):
	even=event.objects.all()

	return render(request,'index.html',{"event":even})
def username_present(user_email,event_sub_category,event):
    if user_reg.objects.filter(Email=user_email,event_sub_category=event_sub_category,event=event).exists():
        return True
    
    return False
def index(request):
	even=event.objects.all()

	return render(request,'index_page.html',{"event":even})

def success(request): 
	return HttpResponse('Registration successful') 

def contact(request):
	return render(request,'contact.html')




def about_us(request):
	return render(request,'aboutus.html')

def user_account(request):
	user=request.user
	user_registration_details=[]
	registration_details=user_reg.objects.filter(Email=user.email)
	
	for register_user in registration_details:
		video=Videos.objects.filter(user_reg=register_user,event=register_user.event)
		image=Images.objects.filter(user_reg=register_user,event=register_user.event)
		video_count=video.count()
		images_count=image.count()
		registration_details={
		"register_user":register_user,
		"image_count":images_count,
		"video_count":video_count,
		"image":image,
		"video":video
		}
		user_registration_details.append(registration_details)
	print (user_registration_details)
	return render(request,'user_account.html',{'registration_details':user_registration_details})


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
			to_email = str(form.cleaned_data.get('email'))
			print("Uid",urlsafe_base64_encode(force_bytes(user.pk)),"Token:",account_activation_token.make_token(user))
			send_mail(email_subject, message,'info@vyomamotionpictures.com',[to_email])
			# email.send()
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
def payment(request,bill_amount=None):
	
	user = request.user
	settings.USER = user
	MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
	MERCHANT_ID = settings.PAYTM_MERCHANT_ID
	# REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
	CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL + request.user.username + '/'
	# Generating unique temporary ids
	order_id = Checksum.__id_generator__()

	bill_amount = bill_amount
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

		return param_dict
	return "error "

# @login_required
@csrf_exempt
def response(request, user_id):
	if request.method == "POST":
		try:
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
				payment=PaytmHistory.objects.create(user=User.objects.get(username=user_id), **data_dict)
				payment.save()
				# user=User.objects.get(username=user_id)
				# event_registration=user_reg(PaytmHistory=PaytmHistory.objects.get(pk=payment.pk))
				# event_registration.save()
				# print(data_dict["event_ID"])
				# user_update=user_reg.objects.get(Email=user.email)
				# user_update.registration_status="completed"
				# user_update.payment_status="Done"
				# user_update.save()
				print (data_dict)
				if data_dict['STATUS']=='TXN_SUCCESS':
					return render(request, "response.html", {"paytm": data_dict,"user":user_id})
				elif data_dict['BANKTXNID']==0:
					return render('FileUpload.html')
				else:
					return render(request, "response_error.html", {"paytm": data_dict,"user":user_id})

		except:
			return render(request,"Register-now.html")


		else:
			return HttpResponse("checksum verify failed")
	else:
		return HttpResponse("Method \"GET\" not allowed")

	return HttpResponse(status=200)
def FileUpload(request,pk=None,id=None):
	if request.method == 'POST':
		id=id
		pk=pk
		print(pk,id)
		if pk==None or id==None:
			id=request.POST.get('event_id')
			pk=request.POST.get('event_pk')
			print(id,pk)
		for key in request.FILES:
			if key=='FileUpload':
				if request.FILES[key]:
					

				
					for fileimg in request.FILES.getlist(key):
						image=Images(user_reg=user_reg.objects.get(pk=id),event=event.objects.get(pk=pk),image=fileimg)
						image.save()

						
					
			elif key=='FileUploada':
				if request.FILES[key]:
								
					for fileimg in request.FILES.getlist(key):
						# print(fileimg)
						video=Videos(user_reg=user_reg.objects.get(pk=id),event=event.objects.get(pk=pk),video=fileimg)
						video.save()

		
		billing_amount=request.POST.get('data')

		request=request
		
		return render(request, "payment.html", {'paytmdict': payment(request,billing_amount), 'user': request.user})
	
	eve=event.objects.get(pk=pk)
	image_count=Images.objects.filter(user_reg=user_reg.objects.get(pk=id)).count()
	video_count=Videos.objects.filter(user_reg=user_reg.objects.get(pk=id)).count()
	if image_count==0 and video_count==0 :
		image_count=0
		video_count=0

	else:
		image_count=image_count
		video_count=video_count
	return render(request,'fileUpload.html',{"event":eve,"image_count":image_count,"video_count":video_count})


@login_required
def register(request,pk=None):
    

	if request.method == 'POST':

		registration_form={}
		file={}
		
		for key in request.POST:
		  registration_form[key] = request.POST[key]


		
		registration_form.pop("csrfmiddlewaretoken", None)
		# registration_form.pop("event_name", None)
		registration_form.pop("event_category", None)
		registration_form.pop("FileUpload", None)
		registration_form.pop("username",None)
		registration_form.pop("FileUploada",None)
		print(registration_form)
		pk=registration_form['event_id']
		print(pk)
		eve=event.objects.get(pk=pk)

		
		print(registration_form)

		
		try :
			if username_present(registration_form['Email'],registration_form['event_sub_category'],eve)==True:
				error_msg='Error:You are already registered for {}'.format(registration_form['event_name'] +' event with ' +registration_form['event_sub_category']+' sub-category')
				raise Exception(error_msg)
			
			else:
				registration_form.pop("event_name", None)
				registration={**registration_form}
				event_reg=user_reg.objects.create(user=User.objects.get(username=request.user),event=event.objects.get(pk=registration_form['event_id']),identity_proof=request.FILES.get('ph_id_proof'),**registration)
				event_reg.save()
			
		except Exception as error:
			print(error)
			pk=registration_form['event_id']
			return render(request,'Register-now.html',{"event":eve,"error":error})
			


		except:
			print ("restless")
			pk=registration_form['event_id']
			return render(request,'Register-now.html',{"event":eve,"error":error})
			
		return redirect('FileUpload',pk=pk, id=event_reg.pk) 


	
		
	if pk:
		even=event.objects.get(pk=pk)
		try:
			reg_user=user_reg.objects.get(Email=request.user.email)
			print ("regrister_user_id",request.user.email)
		except:
			reg_user=None
			print ("banddddddd")
			pass
		

		return render(request,'Register-now.html',{"event":even,"reg_user":reg_user})


	try:
			reg_user=user_reg.objects.get(Email=request.user.email)
			print ("regrister_user_id",request.user.email)
	except:
			reg_user=None
			print ("banddddddd")
			pass
	return render(request,'Register-now.html',{"reg_user":reg_user})


