from django.db import models

# Create your models here.

class Welcome(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    class Meta:
        verbose_name_plural = 'Welcome'

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    welcome = models.ForeignKey('Welcome', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.text[:50]