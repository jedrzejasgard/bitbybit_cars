from django.shortcuts import render
from .models import UserPhoneNumber, Car, Conversation, MassageText

# Create your views here.


def add_user(request):
    if request.method == "POST":
        form_data = json.loads(request.POST['form_imput'])
        phone_number = request.POST['phone']
        car_reg = request.POST['car_reg']
        user_list = UserPhoneNumber.objects.filter(phone_number = phone_number)
        car_list = Car.objects.filter(registration_number = car_reg)
        if not user_list:
            UserPhoneNumber.objects.create(phone_number = phone_number, owned_car = car_reg)
            UserPhoneNumber.save()

        if not car_list:
            Car.create(registration_number = car_reg, car_owner = phone_number)
            Car.save()

    else:
        return Response(serializer.data, status=status.HTTP_200_OK)

def new_conversation(request):


