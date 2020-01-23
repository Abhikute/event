"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from event_reg import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
   
   
   path('FileUpload/', views.FileUpload, name ='FileUpload'),
    path('register/', views.register, name ='register'), 
    path('about_us/', views.about_us, name ='about_us'), 
    path('events/', views.events, name ='events'), 
    path('services/', views.services, name ='services'), 
    path('contact/', views.contact, name ='contact'), 
    
    # path(r'^login/$', view.login),
     path('event_details/', views.event_details, name ='event_details'),
    path('success', views.success, name ='success'),
    path('user_account/', views.user_account, name ='user_account'),
    path('', include('event_reg.urls')),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path(r'^payment/', views.payment, name='payment'),
    re_path(r'^response/(?P<user_id>\w+)/(?P<id>\d+)/$', views.response, name='response'),
  

    
   
   
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
