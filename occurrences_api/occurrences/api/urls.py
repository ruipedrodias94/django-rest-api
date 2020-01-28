
from django.contrib import admin
from django.urls import path
from .views import OccurrenceUpdateView, OccurrenceCreateAndView

urlpatterns = [
    path('<int:pk>', OccurrenceUpdateView.as_view(), name='occurrence_detail_update'),
    path('', OccurrenceCreateAndView.as_view(), name='occurrences'),
]
