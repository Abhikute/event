from django.shortcuts import render,redirect 
from .forms import user_geristration_form,SignUpForm
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import event
import json
# Create your views here.
def user_reg(request):
	return render(request,'user_registration.html')
@login_required
def home(request):
	even=event.objects.all()

	return render(request,'index.html',{"event":even})


def success(request): 
    return HttpResponse('Registration successful') 

def contact(request):
	return render(request,'contact.html')

def register(request,pk=None):

	if request.method == 'POST':
		print (request.POST.get('event_name'))

	if pk:
		even=event.objects.get(pk=pk)
		form=user_geristration_form()

		return render(request,'Register-now.html',{"event":even,"form":form})


	form=user_geristration_form()
	return render(request,'Register-now.html',{"form":form})


def about_us(request):
	return render(request,'aboutus.html')


def events(request):
	even=event.objects.all()
	return render(request,'events.html',{"event":even})


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
        print (user)
        login(user)
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')


def login(request):
	return render(request,'registration/login.html')