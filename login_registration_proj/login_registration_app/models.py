from django.db import models
import re
import bcrypt
# Create your models here.
class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(postData['email']) == 0:
            errors ['register_email'] = "You must enter an email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['register_email'] = ("Invalid email address!")
        current_users = Registration.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['register_email'] = "That email already exists"
        if len(postData['password']) < 8:
            errors['register_password'] = "Password should be at least 8 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['register_password'] = "Passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = Registration.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['login_email'] = "User does not exist"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['login_password'] = "Email and password do not match"
        if len(postData['email']) == 0:
            errors['login_email'] = "Email must be entered"
        if len(postData['password']) < 8:
            errors['login_password'] = "Password should be at least 8 characters"
        
        return errors

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistrationManager()