from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=122)
    email = models.EmailField(max_length=122)
    phone = models.CharField(max_length=22,blank=True)
    desc = models.TextField(max_length=122)

    def __str__(self):
        return self.name
