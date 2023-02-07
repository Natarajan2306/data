from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Count)
@admin.register(Mastersheet)
@admin.register(Retail)
@admin.register(Retail_Count)
@admin.register(Financial)
@admin.register(Financial_Count)
@admin.register(Leadfedder)
@admin.register(Leadfedder_Count)


class ViewAdmin(ImportExportModelAdmin):
	pass