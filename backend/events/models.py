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
    event_location = models.ForeignKey(
        "events.Location",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="event_event_location",
    )


class Location(models.Model):
    "Generated Model"
    address1 = models.CharField(
        max_length=256,
    )
    address2 = models.CharField(
        max_length=256,
    )
    city = models.CharField(
        max_length=256,
    )
    state = models.CharField(
        max_length=2,
    )
    zip = models.CharField(
        max_length=5,
    )


# Create your models here.
