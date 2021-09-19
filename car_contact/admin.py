from django.contrib import admin
from .models import UserPhoneNumber,Car,MassageText,Conversation

# Register your models here.
admin.site.register(UserPhoneNumber)
admin.site.register(Car)
admin.site.register(MassageText)
admin.site.register(Conversation)