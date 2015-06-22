from django.db import models

class Author(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name
class Blog(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateField()
    author = models.ForeignKey(Author)
    def __str__(self):
        return self.subject







# Create your models here.
