from django.urls import path
from django.views.generic import TemplateView
from .views import index, FlightListView

app_name='flight_scheduler'

urlpatterns = [
    path('', index, name='index'),
    path('flights/', FlightListView.as_view(), name='flights')
]
