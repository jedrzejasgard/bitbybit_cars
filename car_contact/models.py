from django.db import models

# Create your models here.


class UserPhoneNumber(models.Model):
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.phone_number


class Car(models.Model):
    registration_number = models.CharField(max_length=100)
    owner_phone = models.ManyToManyField(UserPhoneNumber)
    def __str__(self):
        return self.registration_number


class Conversation(models.Model):
    conversation_id = models.AutoField
    conversation_date_start = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.conversation_id


class MassageText(models.Model):
    text = models.TextField()
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    in_conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE)
    sender = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return self.text
