from django.contrib import admin

# Register your models here.
from . models import Profile,Appointment

admin.site.register(Profile)
admin.site.register(Appointment)
