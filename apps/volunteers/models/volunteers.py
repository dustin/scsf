from django.core import meta

# Create your models here.

class Volunteer(meta.Model):

    fields = (
        meta.CharField('name', maxlength=128),
        meta.CharField('address1', maxlength=64),
        meta.CharField('address2', maxlength=64, blank=True, null=True),
        meta.CharField('city', maxlength=64),
        meta.PositiveIntegerField('zip'),
        meta.EmailField('email'),
        meta.PhoneNumberField('phone'),
        meta.TextField('info', blank=True, null=True),
    )

    admin = meta.Admin()

    def __repr__(self):
        return self.name + " of " + self.city
