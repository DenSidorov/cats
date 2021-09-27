from django.db import models


class Subscribers(models.Model):
    category = models.CharField(
        max_length=200
    )
    subscribers = models.EmailField(description="Email address")

    def __str__(self):
        return f'{self.category}: {self.subscriber}'
