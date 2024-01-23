from django.db import models


# Create your models here.


# Defining database schema
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()

    # This will show the name of the person in admin panel
    def __str__(self):
        return self.name
