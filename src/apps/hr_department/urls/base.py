from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from apps.hr_department import views
from config.env_variables import MODE

urlpatterns_user = [
    path('draft/', views.UserDraftEmployeeHandler.as_view()),
    path('save/', views.UserSaveEmployeeHandler.as_view()),
]

urlpatterns_admin = [
    # path('draft/', views.FormDraftHandler.as_view()),  # TODO
    path('search/', views.SearchHandler.as_view()),  # TODO
]

if MODE != 'local':
    router = DefaultRouter()
    search = router.register(r'search_employers',
                            views.ServerSearchEmployeeInformationDocumentViewSet,
                            basename='searversearchdocument')

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('admin/', include(urlpatterns_admin)),
    path('test/', views.test)
]

if MODE != 'local':
    urlpatterns += router.urls

