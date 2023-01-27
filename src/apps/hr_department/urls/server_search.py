from rest_framework.routers import DefaultRouter

from apps.hr_department import views

router = DefaultRouter()
search = router.register(r'search_employers',
                         views.ServerSearchEmployeeInformationDocumentViewSet,
                         basename='searversearchdocument')
urlpatterns = router.urls
