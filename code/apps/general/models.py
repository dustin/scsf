from django.db import models

class School(models.Model):
    name=models.CharField(max_length=64)
    address1=models.CharField(max_length=64)
    address2=models.CharField(max_length=64, blank=True, null=True)
    city=models.CharField(max_length=64)
    state=models.CharField(max_length=64)
    zip=models.CharField(max_length=64)
    phone=models.CharField(max_length=64)
    fax=models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['name']

class Grade(models.Model):
    name=models.CharField(max_length=32)
    seq=models.IntegerField()

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['seq', 'id']

