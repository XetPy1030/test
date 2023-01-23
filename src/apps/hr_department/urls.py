from django.urls import path, include

from apps.hr_department import views

urlpatterns_user = [
    path('draft/', views.UserDraftEmployeeHandler.as_view()),
    path('save/', views.UserSaveEmployeeDraftHandler.as_view()),
]

urlpatterns_admin = [
    # path('draft/', views.FormDraftHandler.as_view()),  # TODO
    # path('save/', views.SearchHandler.as_view()),  # TODO
    path('search/', views.SearchHandler.as_view()),
]

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('admin/', include(urlpatterns_admin)),
]

