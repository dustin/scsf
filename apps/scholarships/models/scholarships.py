from django.core import meta
from scsf.apps.general.models.general import School

# Create your models here.

class Scholarship(meta.Model):
    year=meta.IntegerField()
    name=meta.CharField(maxlength=64)
    school=meta.ForeignKey(School)

    class META:
        admin = meta.Admin()

        ordering = ['-year', 'name']

    def __repr__(self):
        return "%s in %d" % (self.name, self.year)
