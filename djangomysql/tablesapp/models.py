# tablesapp/models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    semester = models.IntegerField()
    contact_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
