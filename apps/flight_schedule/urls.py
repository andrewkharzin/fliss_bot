from django.urls import path
from django.views.generic import TemplateView

app_name='flight_scheduler'

urlpatterns = [
    path('flight_schedule/', TemplateView.as_view(template_name="flight_schedule/index.html")),
]
