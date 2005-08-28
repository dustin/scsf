from django.core import meta
from scsf.apps.general.models.general import School

# Create your models here.

class WhenToHelp(meta.Model):

    name=meta.CharField(maxlength=64)

    class META:
        admin = meta.Admin()

        verbose_name_plural = "When to Help"

        ordering = ['id']

    def __repr__(self):
        return self.name

class PhoneVolunteer(meta.Model):

    timestamp=meta.DateTimeField('date added', auto_now_add=1)
    name=meta.CharField(maxlength=128)
    address=meta.CharField(maxlength=128)
    city=meta.CharField(maxlength=64)
    zipcode=meta.PositiveIntegerField()
    email=meta.EmailField()
    phone=meta.PhoneNumberField()
    school=meta.ForeignKey(School)
    whentohelp=meta.ManyToManyField(WhenToHelp, radio_admin=True)

    class META:
        admin = meta.Admin(
            list_display=('name', 'city', 'email', 'school',
                'get_whentohelp_list', 'timestamp'),
            )

        ordering = ['-timestamp']

    def __repr__(self):
        return self.name + " of " + self.city
