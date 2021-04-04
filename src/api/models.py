from django.db import models

# Create your models here.
class MiniEgg(models.Model):
    title = models.TextField()

class FinishedEgg(models.Model):
    title = models.TextField()