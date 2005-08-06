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
        meta.IntegerField('seq'),
    )

    admin = meta.Admin()

    ordering = ['seq', 'id']

    def __repr__(self):
        return self.name

