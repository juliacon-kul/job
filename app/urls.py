from app.views import ElementDetail
from app.views import ElementList, ElementDataList
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', ElementList.as_view(), name='element-list'),
    path('data/', ElementDataList.as_view(), name = 'elementdata-list'),
    path('<int:pk>/', ElementDetail.as_view(), name='element-detail'),
]