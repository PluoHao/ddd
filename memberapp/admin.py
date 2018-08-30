from django.contrib import admin
from .models import *
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    list_filter = ['title']


admin.site.register(GoodType)
admin.site.register(Goods,EntryAdmin)
