from django.conf import settings
from django.db import models

class Book(models.Model):
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200, unique=True)
    authors = models.TextField(max_length=500, help_text='Separate each item by comma.')
    tags = models.TextField(help_text='Separate each item by comma.', blank=True, null=True)
    publisher = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, unique=True)
    shelf = models.CharField(max_length=10)
    code = models.CharField(max_length=10, unique=True)
    copies = models.PositiveIntegerField()
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name', 'code']

    def __str__(self):
        return self.name

    def get_authors(self):
        return self.authors.split(',')

    def get_tags(self):
        return self.tags.split(',')

    def get_absolute_url(self):
        return f"/books/{self.pk}"
