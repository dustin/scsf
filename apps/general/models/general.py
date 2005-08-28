from django.core import meta

# Create your models here.

class School(meta.Model):
    name=meta.CharField(maxlength=64)
    address1=meta.CharField(maxlength=64)
    address2=meta.CharField(maxlength=64, blank=True, null=True)
    city=meta.CharField(maxlength=64)
    state=meta.CharField(maxlength=64)
    zip=meta.CharField(maxlength=64)
    phone=meta.CharField(maxlength=64)
    fax=meta.CharField(maxlength=64)

    class META:
        ordering = ['name']

        admin = meta.Admin()

    def __repr__(self):
        return self.name

class Grade(meta.Model):
    name=meta.CharField(maxlength=32)
    seq=meta.IntegerField()

    class META:
        admin = meta.Admin()

        ordering = ['seq', 'id']

    def __repr__(self):
        return self.name

