from django.core import meta

# Create your models here.

class Priority(meta.Model):
    name=meta.CharField(maxlength=128)

    class META:
        ordering = ['name']

        admin = meta.Admin()

        verbose_name_plural='Priorities'

    def __repr__(self):
        return self.name

class Donation(meta.Model):
    ts=meta.DateTimeField('donation timestamp', auto_now_add=1)
    name=meta.CharField(maxlength=128)
    amt=meta.FloatField(max_digits=7, decimal_places=2)
    address1=meta.CharField(maxlength=64, null=True, blank=True)
    address2=meta.CharField(maxlength=64, null=True, blank=True)
    city=meta.CharField(maxlength=64, null=True, blank=True)
    zipcode=meta.PositiveIntegerField(null=True, blank=True)
    email=meta.EmailField(null=True, blank=True)
    phone=meta.PhoneNumberField(null=True, blank=True)
    priorities=meta.ManyToManyField(Priority, blank=True, null=True)
    info=meta.TextField(blank=True, null=True)
    completed=meta.NullBooleanField()

    class META:
        admin = meta.Admin(
            search_fields=('name'),
            list_display=('name', 'city', 'amt', 'completed'),
            list_filter=('ts', 'completed'),
            )

    def __repr__(self):
        return "%s's donation of %.2f on %s" % (self.name, self.amt,
            self.ts.isoformat())
