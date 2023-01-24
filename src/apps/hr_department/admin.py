from django.contrib import admin

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation

# Register your models here.

admin.site.register(ServerEmployeeInformation)
admin.site.register(DraftEmployeeInformation)