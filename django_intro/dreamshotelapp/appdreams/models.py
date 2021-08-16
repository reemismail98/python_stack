from datetime import datetime
from django.db import models
from django.db.models.base import Model
from time import gmtime, strftime
from datetime import date
import re


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        regex=re.compile(r'^[a-zA-Z]+$')
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):           
        #     errors['email'] = "Invalid email address!"
        if len(postData['first_name']) < 2 :
            errors["first_name"] = "First Name should be at least 2 characters and letters only"
        if len(postData['last_name']) < 2 :
            errors["last_name"] = "Last Name should be at least 2 characters and letters only" 
        if len(postData['mobile']) < 10:
            errors['mobile']="Please enter a valid mobile number"    
        return errors 
    def login_validator(self, postData):
        errors = {}
        # date_format = "%Y-%m-%d"
        # a = datetime.strptime(postData['check_in'], date_format)
        # b = datetime.strptime(postData['check_out'], date_format)
        # delta = b - a
        # print (delta.days)
        if postData['check_in'].replace("-", "") < strftime("%Y%m%d", gmtime()):
            errors["check_in"] = "should grather than current date!"
        # if postData['check_out'].replace("-", "") < strftime("%Y%m%d %H:%M %p", gmtime()):
        #     errors["check_out"] = "Invalide Date!"   
        if postData['check_in'] > postData['check_out']:
            errors["check_in_out"] = "check out date should  grather than check in date!"     
        # if postData['adults'] < 0:
        #     errors["adults"] = "Adults grather then 0"
        return errors   

class Hotel(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


class Room(models.Model):
    desc=models.TextField()
    room_name=models.CharField(max_length=255)
    price=models.IntegerField()
    booking_by=models.ManyToManyField(Customer,through="Reversation") 
    hotel=models.ForeignKey(Hotel,related_name="hotelrooms",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reversation(models.Model):
    customer=models.ForeignKey(Customer, related_name="reversation_customer", on_delete = models.CASCADE)
    room=models.ForeignKey(Room, related_name="reversation_room", on_delete = models.CASCADE)
    hotel=models.ForeignKey(Hotel, related_name="reversation_hotel", on_delete = models.CASCADE)
    check_in=models.DateField()
    check_out=models.DateField()
    total_price=models.IntegerField()


class RoomAvalability(models.Model):
    room=models.ForeignKey(Room,related_name="Avalability",on_delete=models.CASCADE)
    reserved_date=models.DateField()
    is_booked=models.BooleanField(default=False)


# def create_booking(first_name,last_name,phone,email):
#     new_booking=Customer.objects.create(first_name=first_name,last_name=last_name,phone=phone,email=email)
#     return new_booking
