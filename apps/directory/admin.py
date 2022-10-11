from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.directory.models import Airline, Register


@admin.register(Airline)
class AilineAdmin(ImportExportModelAdmin):
    list_display = [
        
        'iata',
        'icao',
        'rus_code',
        'comment_eng',
        'comment_rus',
        'country',
        'alliance',
        'lowcost',
        'description',
        'logo',

        
    ]
    search_fields = ['comment_rus','icao']
    # list_editable = [
    #     'rus_name',
    #     'comment',
    #     'comment_rus',
    #     'public_name_eng',
    #     'public_name_rus'
        
    # ]
    
@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    list_display = [
        
        'number',
        'ac_type',
        'co',
        'mod',
        'g_type',
        'description'

        
    ]