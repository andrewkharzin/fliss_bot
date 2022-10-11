from django.contrib import admin
from apps.flight_schedule.models import FlightTask
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(FlightTask)
class TaskAdmin(ImportExportModelAdmin):
    @admin.display(description='task_date')
    def admin_task_date(self, obj):
        return obj.task_date.strftime('%d/%m/%Y')
    @admin.display(description='sched_time')
    def admin_sched_time(self, obj):
        return obj.sched_time.strftime('%H:%M')
    
    list_display = [
        'id',
        'user',
        'admin_task_date',
        'sched_time',
        'technology',
        'airline',
        'registration',
        'admin_sched_time'
        


        
    ]
    link_display = [
        'slug'
    ]


    
  
    
