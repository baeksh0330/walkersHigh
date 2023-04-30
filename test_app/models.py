from django.db import models

# Create your models here.

class Test(models.Model):
    test = models.CharField(max_length=10)

    def __str__(self):
        return self.test

# class Account(models.Model):
#     account = models.CharField(max_length=10)
#     def __acc__(self):
#         return account
#
# class Register(models.Model):
#     register = models.CharField(max_length=10)
#     def __reg__(self):
#         return register


class Person(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    #CharField: 최대길이 정의가 필요한 타입