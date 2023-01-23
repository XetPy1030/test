from django import forms

from apps.hr_department.models import EmployeeInformation


class EmployeeInformationForm(forms.ModelForm):
    class Meta:
        model = EmployeeInformation
        fields = "__all__"
