from django.db import models
from scsf.apps.general.models import School

class Scholarship(models.Model):

    year=models.IntegerField()
    name=models.CharField(maxlength=64)
    school=models.ForeignKey(School)

    class Admin:
        ordering = ['-year', 'name']

    def __str__(self):
        return "%s in %d" % (self.name, self.year)
