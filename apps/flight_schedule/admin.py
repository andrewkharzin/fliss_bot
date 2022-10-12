from django.contrib import admin
from apps.flight_schedule.models import FlightTask
from import_export.admin import ImportExportModelAdmin
from apps.directory.models import Register
from .forms import TaskForm



# Register your models here.
@admin.register(FlightTask)
class TaskAdmin(ImportExportModelAdmin):
    form  = TaskForm
    @admin.display(description='task_date')
    def admin_task_date(self, obj):
        return obj.task_date.strftime('%d/%m/%Y')
    @admin.display(description='sched_time')
    def admin_sched_time(self, obj):
        return obj.sched_time.strftime('%H:%M')
    
    list_display = [
        'user',
        'technology',
        'airline',
        'registration',
        'admin_task_date',
        'admin_sched_time',
        


        
    ]
    link_display = [
        'technology'
    ]
    
    def get_ac(self, obj):
        return obj.register.ac_type
    

    


    
  
    
