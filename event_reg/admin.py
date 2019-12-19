from django.contrib import admin

# Register your models here.
from .models import event,user_reg,PaytmHistory,Images,Videos
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# admin.site.register(user_reg)
# admin.site.register(PaytmHistory)
admin.site.site_header="Administrator"

# admin.site.register(Images)
admin.site.register(Videos)


class viewAdmin(ImportExportModelAdmin):
	list_display=('user','ORDERID','TXNID','TXNDATE','BANKTXNID','BANKNAME','RESPCODE','TXNAMOUNT','STATUS')
	# list_filter=('STATUS')
	search_fields=('user','ORDERID','TXNID','TXNDATE','BANKTXNID','BANKNAME','RESPCODE','TXNAMOUNT','STATUS')
	
class eventview(ImportExportModelAdmin):
	list_display=('event_name','event_category','event_location','event_start_date','event_end_date')
	list_filter=('event_name','event_location','event_start_date','event_end_date')
	search_fields=('event_name','event_location','event_start_date','event_end_date')
	
		
class view_detials(ImportExportModelAdmin):
	list_display=( 'user','event_sub_category', 'first_name', 'Last_name', 'Email', 'gender', 'age', 'mobile', 'alternamte_mobile', 'marital_status', 'birthdate', 'address', 'city', 'state', 'pincode' )
	# list_filter=('STATUS')
	search_fields=('user', 'event_sub_category', 'first_name', 'Last_name', 'Email', 'gender', 'age', 'mobile', 'alternamte_mobile', 'marital_status', 'birthdate', 'address', 'city', 'state', 'pincode')
		
class Images_view(ImportExportModelAdmin):
	list_display=( 'user_reg', 'image')
	# list_filter=('STATUS')
	search_fields=( 'user_reg', 'image')

admin.site.register(PaytmHistory,viewAdmin)
admin.site.register(event,eventview)
admin.site.register(user_reg,view_detials)
admin.site.register(Images,Images_view)

