from django.db import models
from django.core.mail import send_mail
from django.conf import settings

from scsf.apps.general.models import School, Grade

# Create your models here.

class GrantRequest(models.Model):

    req_date=models.DateTimeField('date requested', auto_now_add=1)
    requestor_name=models.CharField(maxlength=64)
    requestor_email=models.EmailField()
    school=models.ForeignKey(School)
    grade=models.ForeignKey(Grade)
    subject=models.CharField(maxlength=64)
    proposal=models.TextField()
    # Number of children that will be benefitted
    benefits=models.PositiveIntegerField()
    principal_notified=models.BooleanField()
    amt_requested=models.FloatField(max_digits=7, decimal_places=2)
    amt_raised=models.FloatField(max_digits=7, decimal_places=2,
        blank=True, null=True)
    raise_description=models.TextField(blank=True, null=True)
    # Null means not processed
    accepted=models.NullBooleanField()
    amt_granted=models.FloatField(max_digits=7, decimal_places=2,
        blank=True, null=True)
    note=models.TextField(blank=True, null=True)

    def save(self):
        is_new = self.id is None
        super(GrantRequest, self).save()
        if is_new:
            if self.principal_notified:
                pn="Principal was notified"
            else:
                pn="Principal was NOT notified"

            mailbody = "School:  %s\nTeacher:  %s <%s>\nAmount:  %.2f\nAffects %d kids\n%s\n\n%s" \
                % (self.school, self.requestor_name, self.requestor_email,
                    self.amt_requested, self.benefits, pn,
                    self.proposal)
            send_mail('New Grant Request - ' + self.subject,
                mailbody, 'noelani+grantrequest@spy.net',
                settings.GRANT_MAIL, fail_silently=True)

    def __str__(self):
        return self.req_date.isoformat() + '_' + self.requestor_name

    class Admin:
        search_fields=('requestor_name', 'proposal')
        list_display=('id', 'req_date', 'requestor_name',
            'amt_requested', 'amt_granted', 'accepted', 'school')
        list_filter=('req_date', 'accepted')
        fields=(
            ('Request Information',
                {'fields': ('req_date', 'requestor_name',
                    'requestor_email', 'school', 'grade', 'subject',
                    'proposal', 'amt_requested', 'amt_raised',
                    'raise_description', 'benefits', 'principal_notified')
                }),
            ('Administrative Options',
                { 'fields': ('accepted', 'amt_granted', 'note')}
            ))
