from django.contrib import admin

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation

admin.site.register(ServerEmployeeInformation)
admin.site.register(DraftEmployeeInformation)
