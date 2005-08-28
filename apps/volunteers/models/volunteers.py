from django.core import meta

# Create your models here.

class Volunteer(meta.Model):

    name=meta.CharField(maxlength=128)
    address1=meta.CharField(maxlength=64)
    address2=meta.CharField(maxlength=64, blank=True, null=True)
    city=meta.CharField(maxlength=64)
    zipcode=meta.PositiveIntegerField()
    email=meta.EmailField()
    phone=meta.PhoneNumberField()
    info=meta.TextField(blank=True, null=True)

    class META:
        admin = meta.Admin()

    def __repr__(self):
        return self.name + " of " + self.city
