from django.http import HttpResponse


def index(request):
    return HttpResponse("It's not working! Timur is a bad programmer!")
