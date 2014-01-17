from django.contrib import admin
from activity.models import *

def export_csv(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(mimetype='text/csv')
	response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		smart_str(u"name"),
		smart_str(u"user"),
	])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.name),
			smart_str(obj.user),
		])
	return response
export_csv.short_description = u"Export CSV"

def export_csvUserData(modeladmin, request, queryset):
	import csv
	from django.utils.encoding import smart_str
	from django.http import HttpResponse
	response = HttpResponse(mimetype='text/csv')
	response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
	writer.writerow([
		smart_str(u"name"),
		smart_str(u"user"),
	])
	for obj in queryset:
		writer.writerow([
			smart_str(obj.name),
			smart_str(obj.user),
		])
	return response

class ActivityAdmin(admin.ModelAdmin):
	actions = [export_csv]
	#actions = [export_csv, export_xls, export_xlsx]

class ActivityInstanceAdmin(admin.ModelAdmin):
	pass

class RateActivityAdmin(admin.ModelAdmin):
	pass

class RateActivityInstanceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityInstance, ActivityInstanceAdmin)
admin.site.register(RateActivity, RateActivityAdmin)
admin.site.register(RateActivityInstance, RateActivityInstanceAdmin)
