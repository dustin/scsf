from django.core import meta
from scsf.apps.general.models.general import School

# Create your models here.

class WhenToHelp(meta.Model):

    fields = (
        meta.CharField('name', maxlength=64),
    )

    admin = meta.Admin()

    verbose_name_plural = "When to Help"

    ordering = ['id']

    def __repr__(self):
        return self.name

class PhoneVolunteer(meta.Model):

    fields = (
        meta.DateTimeField('timestamp', 'date added', auto_now_add=1),
        meta.CharField('name', maxlength=128),
        meta.CharField('address', maxlength=128),
        meta.CharField('city', maxlength=64),
        meta.PositiveIntegerField('zip'),
        meta.EmailField('email'),
        meta.PhoneNumberField('phone'),
        meta.ForeignKey(School),
        meta.ManyToManyField(WhenToHelp, radio_admin=True),
    )

    admin = meta.Admin(
        list_display=('name', 'city', 'email', 'get_school',
            'get_whentohelp_list', 'timestamp'),
        )

    ordering = ['-timestamp']

    def __repr__(self):
        return self.name + " of " + self.city
