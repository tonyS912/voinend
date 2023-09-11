from django.db import models


class Contacts(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
