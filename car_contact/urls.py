from django.urls import path

from . import views

urlpatterns = [
    path('add_user/',views.add_user, name = 'add_user'),
    path('send_massage/',views.send_massage, name = 'send_massage'),
    path('check_conversation',views.check_conversation, name= 'check_conversation'),
]