from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def isValidRegistration(self, userInfo, request):
        passFlag = True
        if not userInfo['first_name'].isalpha():
            messages.warning(
                request, 'First name contains non-alpha character(s)')
            passFlag = False
        if len(userInfo['first_name']) < 2:
            messages.warning(request, 'First name is not long enough.')
            passFlag = False
        if not userInfo['last_name'].isalpha():
            messages.warning(
                request, 'Last name contains non-alpha character(s)')
            passFlag = False
        if len(userInfo['last_name']) < 2:
            messages.warning(request, 'Last name is not long enough.')
            passFlag = False
        if not EMAIL_REGEX.match(userInfo['email']):
            messages.warning(request, 'Email is not a valid email!')
            passFlag = False
        if len(userInfo['password']) < 7:
            messages.warning(request, 'Password is not long enough.')
            passFlag = False
        if userInfo['password'] != userInfo['confirm_password']:
            messages.warning(request, 'Password match not confirmed.')
            passFlag = False
        if User.objects.filter(email=userInfo['email']):
            messages.error(
                request, "This email already exists in our database.")
            passFlag = False

        if passFlag == True:
            messages.success(request, "Success! Welcome, " +
                             userInfo['first_name'] + "!")
            hashed = bcrypt.hashpw(
                userInfo['password'].encode(), bcrypt.gensalt())
            User.objects.create(
                first_name=userInfo['first_name'], last_name=userInfo['last_name'], email=userInfo['email'], password=hashed)
        return passFlag

    def UserExistsLogin(self, userInfo, request):
        passFlag = True
        if User.objects.filter(email=userInfo['email']):
            hashed = User.objects.get(email=userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.success(request, "Success! Welcome, " +
                                 User.objects.get(email=userInfo['email']).first_name + "!")
                passFlag = True
            else:
                messages.warning(
                    request, "Unsuccessful login. Incorrect password")
                passFlag = False
        else:
            messages.warning(
                request, "Unsuccessful login. Your email is incorrect.")
            passFlag = False
        return passFlag


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
    objects = models.Manager()
