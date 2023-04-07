from django.contrib import admin

from .models import *

class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

admin.site.register(Catagory, CatergoryAdmin)
admin.site.register(Product)
