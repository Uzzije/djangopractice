from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, default='')

    def __unicode__(self):
        return self.user.username

class Blog(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateField()
    author = models.ForeignKey(Author)
    def __unicode__(self):
        return self.subject






# Create your models here.
