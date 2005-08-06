from django.core import meta
from scsf.apps.general.models.general import School, Grade

# Create your models here.

class GrantRequest(meta.Model):

    fields = (
        meta.DateTimeField('req_date', 'date requested', auto_now_add=1),
        meta.CharField('requestor_name', maxlength=64),
        meta.EmailField('requestor_email'),
        meta.ForeignKey(School),
        meta.ForeignKey(Grade),
        meta.CharField('subject', maxlength=64),
        meta.TextField('proposal'),
        # Number of children that will be benefitted
        meta.PositiveIntegerField('benefits'),
        meta.BooleanField('principal_notified'),
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

    admin = meta.Admin(
        search_fields=('requestor_name', 'proposal'),
        list_display=('req_date', 'requestor_name',
            'amt_requested', 'amt_granted', 'accepted', 'get_school'),
        list_filter=('req_date', 'accepted'),
        fields=(
            ('Request Information',
                {'fields': ('requestor_name',
                    'requestor_email', 'school_id', 'grade_id', 'subject',
                    'proposal', 'amt_requested', 'amt_raised',
                    'raise_description', 'benefits', 'principal_notified')
                }),
            ('Administrative Options',
                { 'fields': ('accepted', 'amt_granted', 'note')}
            )),
        )

    def __repr__(self):
        return self.req_date.isoformat() + '_' + self.requestor_name
