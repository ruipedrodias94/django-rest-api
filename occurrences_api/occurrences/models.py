from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse


# Create your models here.


class OccurrenceModel(models.Model):
    """
    Occurrence Model
    - User
    - Description
    - Latitude
    - Longitude
    - Creation date
    - Update date
    - State (POR_VALIDAR, VALIDADO, RESOLVIDO)
    - Category (CONSTRUCTION, SPECIAL_EVENT, INCIDENT, WEATHER_CONDITION, ROAD_CONDITION)
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_created=True, blank=True, null=True)
    state = models.TextField(max_length=20, null=True, blank=True, default="POR_VALIDAR")
    category = models.TextField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self, request=None):
        return reverse("api_occurrences:occurrence_detail_update", kwargs={'pk': self.pk}, request=request)
