from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name_plural = 'About'

class Biography(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    bio = models.TextField()
    email = models.EmailField()
    phone = PhoneNumberField()
    order = models.IntegerField()

    def __str__(self):
        return self.name + ', ' + self.title

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Biographies'