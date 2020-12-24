from django.db import models

class Articles(models.Model):
    """docstring for Articles."""
    title = models.CharField(max_length = 255)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


# Create your models here.
