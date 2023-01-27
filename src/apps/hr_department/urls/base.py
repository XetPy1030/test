from django.urls import path, include
from apps.hr_department import views

urlpatterns_user = [
    path('draft/', views.UserDraftEmployeeHandler.as_view()),
    path('save/', views.UserSaveEmployeeHandler.as_view()),
]

urlpatterns_admin = [
    # path('draft/', views.FormDraftHandler.as_view()),  # TODO
    path('search/', views.SearchHandler.as_view()),  # TODO
]

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('admin/', include(urlpatterns_admin)),
    path('test/', views.test)
]

