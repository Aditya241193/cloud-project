from django.db import models

class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100,default="",null=True,blank=True)
    state = models.CharField(max_length=10,default="",null=True,blank=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
