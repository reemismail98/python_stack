from django.db import models

# Create your models here.
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
    def book_validator(self,postData):
        errors = {}
        books = Books.objects.filter(title=postData['title'])
        if not postData['title']:
            errors['title'] = "Title is required!"
        if len(books):
            errors['title'] = "Book already added!"
        if len(postData['desc'])< 5:
            errors['desc'] = "Description should be at least 5 characters"
        return errors


class Users(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255) 
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

class Books(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    uploded_by=models.ForeignKey(Users,related_name="books", on_delete = models.CASCADE)
    favbookuser = models.ManyToManyField(Users, related_name="favbook")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()



def register(firstnames,lastname,email,password):
    Users.objects.create(firstname=firstnames,lastname=lastname,email=email,password=password)


def book_liked_by(user_id,book_id):
    book = Books.objects.get(id=book_id)
    book_liked_by = book.user_liked.all()
    users = book_liked_by.filter(id=user_id)
    return users
