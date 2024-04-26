from django.contrib import admin
from .models import YD_Car, YD_Customer, YD_Class, YD_Employee, YD_Location, YD_Model

admin.site.register(YD_Car)
admin.site.register(YD_Customer)
admin.site.register(YD_Class)
admin.site.register(YD_Employee)
admin.site.register(YD_Location)
admin.site.register(YD_Model)