from django.db import models

# Create your models here.

class ContactUsModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name

    # use verbose name plural , change the model name
    # class Meta:
    #     verbose_name_plural = 'ModelNames'
    