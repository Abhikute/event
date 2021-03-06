from django.contrib import admin

# Register your models here.
from .models import event,user_reg,PaytmHistory,Images,Videos,Temp_Videos,Temp_Images
import json
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(user_reg)
# admin.site.register(PaytmHistory)
admin.site.site_header="Administrator"

# admin.site.register(Images)
admin.site.register(Videos)
admin.site.register(Temp_Videos)
admin.site.register(Temp_Images)
class viewAdmin(ImportExportModelAdmin):
	list_display=('user','user_reg','ORDERID','TXNID','TXNDATE','BANKTXNID','BANKNAME','RESPCODE','TXNAMOUNT','STATUS')
	list_filter=('user','TXNDATE','BANKNAME','STATUS')
	search_fields=('ORDERID','TXNID','TXNDATE','BANKTXNID')
	
	
class eventview(ImportExportModelAdmin):
	list_display=('event_name','event_category','event_location','event_start_date','event_end_date')
	list_filter=('event_name','event_location','event_start_date','event_end_date')
	search_fields=('event_name','event_location','event_start_date','event_end_date')
	
		
class view_detials(ImportExportModelAdmin):
	list_display=( 'user','event','event_sub_category','first_name', 'Last_name', 'Email', 'gender', 'age', 'mobile', 'alternamte_mobile', 'marital_status', 'birthdate', 'address', 'city', 'state', 'pincode' )
	list_filter=('user','event','event_sub_category','first_name', 'Last_name', 'Email')
	search_fields=('event_sub_category', 'first_name', 'Last_name', 'Email', 'mobile', 'alternamte_mobile',  'city', 'state', 'pincode')
		
class Images_view(ImportExportModelAdmin):
	list_display=( 'user_reg', 'image')
	# list_filter=('STATUS')
	search_fields=( 'user_reg', 'image')

admin.site.register(PaytmHistory,viewAdmin)
admin.site.register(event,eventview)
admin.site.register(user_reg,view_detials)
admin.site.register(Images,Images_view)



