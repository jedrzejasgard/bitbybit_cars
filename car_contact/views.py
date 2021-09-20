from django.shortcuts import render
from .models import UserPhoneNumber, Car, Conversation, MassageText
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def add_user(request):
    if request.method == "POST":
        model = User
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

def send_massage(request):
    if request.method == "POST":
        text = request.POST['text']
        in_conversation = request.POST['conversation_id']
        # check logged user and auto fill
        sender = 'Sender to by filed...'
        send_to = request.POST['send_to']
        conversations = Conversation.objects.filter(conversation_id = in_conversation)
        if not conversations:
            new_conversation = Conversation.object.create(participants_car_1 = sender, participants_car_2 = send_to)
            new_conversation.save()
        else:
            MassageText.object.create()
        return JsonResponse(status=201, data={'status': '201_created'})

    else:
        return JsonResponse(status=400, data={'status': '400_bad_request'})

