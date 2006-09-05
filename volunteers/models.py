from django.db import models

# Create your models here.
class Volunteer(models.Model):

    name=models.CharField(maxlength=128)
    address1=models.CharField(maxlength=64)
    address2=models.CharField(maxlength=64, blank=True, null=True)
    city=models.CharField(maxlength=64)
    zipcode=models.PositiveIntegerField()
    email=models.EmailField()
    phone=models.PhoneNumberField()
    info=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " of " + self.city

    class Admin:
        pass
