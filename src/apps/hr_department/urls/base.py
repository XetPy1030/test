from django.urls import path, include
from apps.hr_department import views

urlpatterns_user = [
    path('draft/', views.UserDraftHandler.as_view()),
    path('save/', views.UserSaveHandler.as_view()),
]

urlpatterns_admin = [
    path('draft/', views.AdminDraftHandler.as_view()),
    path('save/', views.AdminSaveHandler.as_view()),
    path('search/', views.SearchHandler.as_view()),
]

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('admin/', include(urlpatterns_admin)),
    # path('test/', views.test)
]

