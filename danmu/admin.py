from django.contrib import admin
from  danmu.models import DanmuModel
# Register your models here.
class DanmuAdmin(admin.ModelAdmin):
    list_display = ['name','message','send_time_float']


admin.site.register(DanmuModel,DanmuAdmin)