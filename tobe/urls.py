from django.urls import path , include
from.views import TobeCreate , TobeDelete , TobeDetail , TobeEdit , TobeList
from.api import TobeViewset
from rest_framework.routers import DefaultRouter

app_name = 'tobe'
router = DefaultRouter()
router.register('',TobeViewset)

urlpatterns = [
    path('api/',include(router.urls)),
     path('tobe/<int:pk>/',TobeDetail.as_view()),
    path('tobe/',TobeList.as_view()),
    path('tobe/<int:pk>/delete',TobeDelete.as_view()),
    path('tobe/<int:pk>/edit',TobeEdit.as_view()),
    path('tobe/new',TobeCreate.as_view()),
]
