from django.db import models

class Notes(models.Model):
    title = models.TextField()
    description = models.TextField()
