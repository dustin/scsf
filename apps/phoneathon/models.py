from django.db import models
from scsf.apps.general.models import School

class WhenToHelp(models.Model):

    name=models.CharField(maxlength=64)

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['id']

    class Meta:
        verbose_name_plural = "When to Help"

class PhoneVolunteer(models.Model):

    timestamp=models.DateTimeField('date added', auto_now_add=1)
    name=models.CharField(maxlength=128)
    address=models.CharField(maxlength=128)
    city=models.CharField(maxlength=64)
    zipcode=models.PositiveIntegerField()
    email=models.EmailField()
    phone=models.PhoneNumberField()
    school=models.ForeignKey(School)
    whentohelp=models.ManyToManyField(WhenToHelp)

    def __str__(self):
        return self.name + " of " + self.city

    class Admin:
        list_display=('name', 'city', 'email', 'school', 'timestamp')

        ordering = ['-timestamp']

