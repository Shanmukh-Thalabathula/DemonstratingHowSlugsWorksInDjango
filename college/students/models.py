from django.db import models
from django.utils.text import slugify
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=14)
    roll_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name