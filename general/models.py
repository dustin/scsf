from django.db import models

class School(models.Model):
    name=models.CharField(maxlength=64)
    address1=models.CharField(maxlength=64)
    address2=models.CharField(maxlength=64, blank=True, null=True)
    city=models.CharField(maxlength=64)
    state=models.CharField(maxlength=64)
    zip=models.CharField(maxlength=64)
    phone=models.CharField(maxlength=64)
    fax=models.CharField(maxlength=64)

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['name']

class Grade(models.Model):
    name=models.CharField(maxlength=32)
    seq=models.IntegerField()

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['seq', 'id']

