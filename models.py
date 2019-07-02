from django.db import models

# Create your models here.


class candidate(models.Model):
    name = models.CharField(max_length=40, unique=False)

    def __str__(self):
        return  self.name

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30, unique=False)
    name = models.CharField(max_length=40, unique=False)

    def __str__(self):
        return self.name
