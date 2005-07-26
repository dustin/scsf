from django.core import meta
from scsf.apps.general.models.general import School

# Create your models here.

class Scholarship(meta.Model):
    fields = (
        meta.IntegerField('year'),
        meta.CharField('name', maxlength=64),
        meta.ForeignKey(School),
    )

    admin = meta.Admin()

    def __repr__(self):
        return "%s in %d" % (self.name, self.year)
