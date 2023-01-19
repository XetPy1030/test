from django.http import Http404, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.hr_department.forms import EmployeeInformationForm
from apps.hr_department.models import EmployeeInformation


class FormHandler(APIView):
    def get_object(self, pk):
        try:
            return EmployeeInformation.objects.get(pk=pk)
        except EmployeeInformation.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        form = EmployeeInformationForm(request.data)
        print(request.data)
        if form.is_valid():
            form.save()
            return Response(form.data)
        return Response(form.errors)

def index(request):
    return HttpResponse("It's not working! Timur is a bad programmer!")
