from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from apps.hr_department import views
from config.env_variables import MODE

urlpatterns_user = [
    path('draft/', views.UserDraftEmployeeHandler.as_view()),
    path('save/', views.UserSaveEmployeeDraftHandler.as_view()),
]

urlpatterns_admin = [
    # path('draft/', views.FormDraftHandler.as_view()),  # TODO
    # path('save/', views.SearchHandler.as_view()),  # TODO
]

if MODE != 'local':
    router = DefaultRouter()
    books = router.register(r'employers',
                            views.ServerSearchEmployeeInformationDocumentViewSet,
                            basename='searversearchdocument')

    urlpatterns_search = [
        re_path(r'^', include(router.urls)),
    ]
    urlpatterns_admin += [
        path('search_server/', include(urlpatterns_search))
    ]

urlpatterns = [
    path('user/', include(urlpatterns_user)),
    # path('admin/', include(urlpatterns_admin)),
]
