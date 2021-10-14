from django.contrib import admin
from . models import *
admin.site.site_header='Masaeed'
admin.site.register(Whse_Mangament)
admin.site.register(STAFF)
admin.site.register(Tag)

@admin.register(TASKS)
class TASKSModelAdmin(admin.ModelAdmin):
     list_display = ['STAFF', 'Whse_Mangament', 'date_created','status','TASK_NO','my_file',]

@admin.register(FULFILLED)
class FULFILLEDModelAdmin(admin.ModelAdmin):
     list_display = ['STAFF','Whse_Mangament','TASK_NO', 'date_created','status','note']
# Register your models here.
  

# Register your models here.
