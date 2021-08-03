from django.contrib import admin
from dor.models import Contactus
from dor.models import Internship
# Register your models here.

class ContactusAdmin(admin.ModelAdmin):
    list_display=('mail','Name','Issue','Whatshap','Contact','State')

class InternshipAdmin(admin.ModelAdmin):
    list_display=('FirstName','LastName','Email','Contactno','College','InternField')

admin.site.register(Contactus,ContactusAdmin)
admin.site.register(Internship,InternshipAdmin)

