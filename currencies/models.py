import uuid
from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=200, unique=True)
    symbol = models.CharField(max_length=200)
    current_price = models.FloatField(blank=True, null=True)
    percent_change = models.FloatField(blank=True, null=True)
    last_day_lowest_price = models.FloatField(blank=True, null=True)
    last_day_highest_price = models.FloatField(blank=True, null=True)
    last_day_open_price = models.FloatField(blank=True, null=True)
    all_time_highest_price = models.FloatField(blank=True, null=True)
    description = models.TextField(null=True, blank=True, max_length=2000) 
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


