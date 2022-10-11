from django.urls import path
from apps.flight_schedule.flight_schedule_api.views import FlightTaskList



urlpatterns = [
    path('scheduler/', FlightTaskList.as_view(), name="api_scheduler")
]