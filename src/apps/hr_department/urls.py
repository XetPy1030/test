from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from apps.hr_department import views

router = DefaultRouter()
books = router.register(r'search_employers',
                        views.ServerSearchEmployeeInformationDocumentViewSet,
                        basename='searversearchdocument')

urlpatterns_user = [
    path('draft/', views.UserDraftEmployeeHandler.as_view()),
    path('save/', views.UserSaveEmployeeDraftHandler.as_view()),
]

urlpatterns_admin = [
    # path('draft/', views.FormDraftHandler.as_view()),  # TODO
    # path('save/', views.SearchHandler.as_view()),  # TODO
]

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    path('admin/', include(urlpatterns_admin)),
]

urlpatterns += router.urls
