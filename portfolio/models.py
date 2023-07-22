from django.db import models
from django.db.models import URLField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
