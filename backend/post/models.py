from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__():
        return f'title';