import bcrypt
from django.db import models
import re

from django.http import request

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        if "firstname" in postData.keys():
            errors = {}
            regex=re.compile(r'^[a-zA-Z]+$')
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):           
                errors['email'] = "Invalid email address!"
            if len(postData['firstname']) < 2 or not regex.match(postData['firstname']):
                errors["firstname"] = "First Name should be at least 2 characters and letters only"
            if len(postData['lastname']) < 2 or not regex.match(postData['lastname']):
                errors["lastname"] = "Last Name should be at least 2 characters and letters only"
            if len(postData['password']) < 8 :
                errors["password"] = "Password should be at least 8 characters" 
            if postData['password'] != postData['confirm_pw'] :
                errors["confirm"] = "Passwords should be match"    
            return errors 
    def login_validator(self, postData):
        errors1 = {}
        checkemail=postData["email"]
        user=Users.objects.filter(email=checkemail)
        if len(user) < 1:
            errors1["email"] = "Invalid Email or Password"
        if user:
            if not bcrypt.checkpw(postData["password"].encode(),user[0].password.encode()):
                errors1["password"] = "Invalid Email or Password"
        return errors1   

class Users(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255) 
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    # birthday=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()


class Messages(models.Model):
    user_id=models.ForeignKey(Users, related_name="message", on_delete = models.CASCADE)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user_id=models.ForeignKey(Users, related_name="comments", on_delete = models.CASCADE)
    message_id=models.ForeignKey(Messages, related_name="message_comments", on_delete = models.CASCADE)
    comment=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    




