from django.shortcuts import render
from .models import UserPhoneNumber, Car, Conversation, MassageText
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        phone_number = request.POST['phone']
        car_reg = request.POST['car_reg']
        #user_list = UserPhoneNumber.objects.filter(phone_number = phone_number)
        car_list = Car.objects.filter(registration_number = car_reg)
        if not car_list:
            car_obj = Car.objects.create(registration_number = car_reg)
            car_obj.save()
        else:
            car_obj = car_list[0]
            car_obj.owner_phone.create(phone_number = phone_number)

        return JsonResponse(status=201, data={'status':'201_created'})

    else:
        return JsonResponse(status=400, data={'status':'400_bad_request'})

def new_conversation(request):
    pass

