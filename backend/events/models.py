from django.conf import settings
from django.db import models


class Event(models.Model):
    "Generated Model"
    event_name = models.CharField(
        max_length=256,
    )
    event_date = models.DateField(
        null=True,
        blank=True,
    )
    event_description = models.TextField(
        null=True,
        blank=True,
    )
    event_time = models.TimeField(
        null=True,
        blank=True,
    )


# Create your models here.
