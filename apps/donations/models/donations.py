from django.core import meta

# Create your models here.

class Priority(meta.Model):
    fields = (
        meta.CharField('name', maxlength=128),
    )

    ordering = ['name']

    admin = meta.Admin()

    def __repr__(self):
        return self.name

class Donation(meta.Model):
    fields = (
        meta.DateTimeField('ts', 'donation timestamp', auto_now_add=1),
        meta.CharField('name', maxlength=128),
        meta.FloatField('amt', max_digits=7, decimal_places=2),
        meta.CharField('address1', maxlength=64, null=True, blank=True),
        meta.CharField('address2', maxlength=64, null=True, blank=True),
        meta.CharField('city', maxlength=64, null=True, blank=True),
        meta.PositiveIntegerField('zip', null=True, blank=True),
        meta.EmailField('email', null=True, blank=True),
        meta.PhoneNumberField('phone', null=True, blank=True),
        meta.ManyToManyField(Priority, blank=True, null=True),
        meta.TextField('info', blank=True, null=True),
        meta.NullBooleanField('completed'),
    )

    def __repr__(self):
        return "%s's donation of %.2f on %s" % (self.name, self.amt,
            self.ts.isoformat())

    admin = meta.Admin(
        search_fields=('name'),
        list_display=('name', 'city', 'amt', 'completed'),
        list_filter=('ts', 'completed'),
        )
