from django.core import meta
from scsf.apps.general.models.general import School, Grade

# Create your models here.

class GrantRequest(meta.Model):

    req_date=meta.DateTimeField('date requested', auto_now_add=1)
    requestor_name=meta.CharField(maxlength=64)
    requestor_email=meta.EmailField()
    school=meta.ForeignKey(School)
    grade=meta.ForeignKey(Grade)
    subject=meta.CharField(maxlength=64)
    proposal=meta.TextField()
    # Number of children that will be benefitted
    benefits=meta.PositiveIntegerField()
    principal_notified=meta.BooleanField()
    amt_requested=meta.FloatField(max_digits=7, decimal_places=2)
    amt_raised=meta.FloatField(max_digits=7, decimal_places=2,
        blank=True, null=True)
    raise_description=meta.TextField(blank=True, null=True)
    # Null means not processed
    accepted=meta.NullBooleanField()
    amt_granted=meta.FloatField(max_digits=7, decimal_places=2,
        blank=True, null=True)
    note=meta.TextField(blank=True, null=True)

    class META:
        admin = meta.Admin(
            search_fields=('requestor_name', 'proposal'),
            list_display=('id', 'req_date', 'requestor_name',
                'amt_requested', 'amt_granted', 'accepted', 'school'),
            list_filter=('req_date', 'accepted'),
            fields=(
                ('Request Information',
                    {'fields': ('req_date', 'requestor_name',
                        'requestor_email', 'school', 'grade', 'subject',
                        'proposal', 'amt_requested', 'amt_raised',
                        'raise_description', 'benefits', 'principal_notified')
                    }),
                ('Administrative Options',
                    { 'fields': ('accepted', 'amt_granted', 'note')}
                )),
            )

    def __repr__(self):
        return self.req_date.isoformat() + '_' + self.requestor_name
