from django.contrib import admin
from exp.models import ExpModel
# Register your models here.
class ExpAdmin(admin.ModelAdmin):
    list_display = ['name','message']


admin.site.register(ExpModel,ExpAdmin)