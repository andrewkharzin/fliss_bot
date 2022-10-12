import django_tables2 as tables
from .models import FlightTask
 
 
 
class TasksTable(tables.Table):
    
     
    
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    class Meta:
        ATTRIBUTES = {
            "th" : {
                "_ordering": {
                    "orderable": "sortable", # Instead of `orderable`
                    "ascending": "ascend",   # Instead of `asc`
                    "descending": "descend"  # Instead of `desc`
                }
            }
        }
        model = FlightTask
        sequence = ('selection', 'task_date',)
        template_name = "django_tables2/bootstrap.html"
        fields = (
            'user',
            'task_date',
            'technology',
            'airline',
            'flight',
            'sched_time',
            'route',
            'status',
            
        )
        task_date = tables.Column(attrs=ATTRIBUTES) 
 