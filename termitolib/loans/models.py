import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings

from books.models import Book

def get_deadline():
    return datetime.datetime.today() + datetime.timedelta(days=7)


class Loan(models.Model):
    by = models.ForeignKey(settings.AUTH_USER_MODEL)
    to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to')
    item = models.ForeignKey(Book)
    loan_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default=get_deadline)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['loan_date', 'return_date']

    def __str__(self):
        return (self.item.name + ' - ' +self.to.username)

    @property
    def is_late(self):
        if self.return_date < timezone.now():
            return True
        else:
            return False

    def get_absolute_url(self):
        return f"/loans/{self.pk}"
