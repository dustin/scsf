from django.db import models

class Priority(models.Model):

    name=models.CharField(maxlength=128)

    def __str__(self):
        return self.name

    class Admin:
        ordering = ['name']

    class Meta:
        verbose_name_plural='Priorities'

class Donation(models.Model):
    ts=models.DateTimeField('donation timestamp', auto_now_add=1)
    name=models.CharField(maxlength=128)
    amt=models.FloatField(max_digits=7, decimal_places=2)
    address1=models.CharField(maxlength=64, null=True, blank=True)
    address2=models.CharField(maxlength=64, null=True, blank=True)
    city=models.CharField(maxlength=64, null=True, blank=True)
    zipcode=models.PositiveIntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    phone=models.PhoneNumberField(null=True, blank=True)
    priorities=models.ManyToManyField(Priority, blank=True, null=True)
    info=models.TextField(blank=True, null=True)
    completed=models.NullBooleanField()

    def __str__(self):
        return "%s's donation of %.2f on %s" % (self.name, self.amt,
            self.ts.isoformat())

    class Admin:
        search_fields=('name')
        list_display=('name', 'city', 'amt', 'completed')
        list_filter=('ts', 'completed')

