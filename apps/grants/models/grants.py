from django.core import meta

# Create your models here.

class School(meta.Model):
    fields = (
        meta.CharField('name', maxlength=64),
        meta.CharField('address1', maxlength=64),
        meta.CharField('address2', maxlength=64, blank=True, null=True),
        meta.CharField('city', maxlength=64),
        meta.CharField('state', maxlength=64),
        meta.CharField('zip', maxlength=64),
        meta.CharField('phone', maxlength=64),
        meta.CharField('fax', maxlength=64),
    )

    ordering = ['name']

    admin = meta.Admin()

    def __repr__(self):
        return self.name

class Grade(meta.Model):
    fields = (
        meta.CharField('name', maxlength=32),
    )

    admin = meta.Admin()

    ordering = ['id']

    def __repr__(self):
        return self.name

class GrantRequest(meta.Model):

    fields = (
        meta.DateTimeField('req_date', 'date requested', auto_now_add=1),
        meta.CharField('requestor_name', maxlength=64),
        meta.EmailField('requestor_email'),
        meta.ForeignKey(School),
        meta.ForeignKey(Grade),
        meta.CharField('subject', maxlength=64),
        meta.TextField('proposal'),
        meta.FloatField('amt_requested', max_digits=7, decimal_places=2),
        meta.FloatField('amt_raised', max_digits=7, decimal_places=2,
            blank=True, null=True),
        meta.TextField('raise_description', blank=True, null=True),
        # Null means not processed
        meta.NullBooleanField('accepted'),
        meta.FloatField('amt_granted', max_digits=7, decimal_places=2,
            blank=True, null=True),
        meta.TextField('note', blank=True, null=True),
    )

    admin = meta.Admin()

    def __repr__(self):
        return self.req_date.isoformat() + '_' + self.requestor_name
