from django.db import models

# Create your models here.


class Comments(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    profession = models.CharField(
        max_length=100
    )
    picture_url = models.URLField()
    short_message = models.CharField(
        max_length=1000
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
