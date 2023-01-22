from django.urls import path

from apps.hr_department import views

urlpatterns = [
    # path('', views.index)
    path('api/', views.FormDraftHandler.as_view()),
]

