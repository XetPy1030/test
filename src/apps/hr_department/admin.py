from django.contrib import admin

from apps.hr_department.models import ServerEmployeeInformation, DraftEmployeeInformation, Children, Education

admin.site.register(ServerEmployeeInformation)
admin.site.register(DraftEmployeeInformation)
admin.site.register(Children)
admin.site.register(Education)
