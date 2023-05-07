from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user_id = models.CharField(max_length=255)
    image_url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Record'
