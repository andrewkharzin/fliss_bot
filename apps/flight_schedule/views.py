from django.template.response import TemplateResponse
from apps.flight_schedule.models import FlightTask
from django_tables2 import SingleTableView
 
from .tables import TasksTable
 

 
def index(request):
    ftl = FlightTask.postObjects.all()
    context = {
        'ftl': ftl
    }
    
    return TemplateResponse(request, 'index.html', context=context)


class FlightListView(SingleTableView):
    model = FlightTask
    table_class = TasksTable
    template_name = 'table_flights.html'
    # paginator_class = LazyPaginator