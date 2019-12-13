from django.conf.urls import url
from . import views as view

urlpatterns = [
    
        url(r'^register_user/$', view.usersignup, name='register_user'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view.activate_account, name='activate'),
        url(r'^$', view.home, name='home'), 
        url(r'^event_details/(?P<pk>\d+)/$', view.event_details, name ='event_details_with_pk'),
        url(r'^register/(?P<pk>\d+)/$', view.register, name ='register_with_pk'),
        

]