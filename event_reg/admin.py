from django.contrib import admin

# Register your models here.
from .models import registrations,event,user_reg
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(user_reg)
admin.site.site_header="Administrator"


# class viewAdmin(ImportExportModelAdmin):
# 	list_display=('first_name','last_name','age','email','gender','categary','Video_URL','photo',"address")
# 	list_filter=('categary','gender')
# 	search_fields=('first_name','last_name','age','email','gender','categary')
	
class eventview(ImportExportModelAdmin):
	list_display=('event_name','event_category','event_location','event_start_date','event_end_date')
	list_filter=('event_name','event_location','event_start_date','event_end_date')
	search_fields=('event_name','event_location','event_start_date','event_end_date')
	
		
# admin.site.register(Person,viewAdmin)
admin.site.register(event,eventview)
