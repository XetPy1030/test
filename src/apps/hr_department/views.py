from django.http import HttpResponse
from rest_framework.views import APIView

from apps.hr_department.serializers import EmployeeInformationSerializer


class FormHandler(APIView):
    # post for serializer EmployeeInformationSerializer
    def post(self, request):
        serializer = EmployeeInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)
