# from app.views import ElementDetail
# from app.views import ElementList
from app.views import ElementView
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('elements/',ElementView.as_view()),
    path('elements/<int:pk>/',ElementView.as_view()),
    # path('elementsdata/',ElementDataView.as_view()),
    # path('', ElementList.as_view(), name='element-list'),
    # path('data/', ElementDataList.as_view(), name = 'elementdata-list'),
    # path('<int:pk>/', ElementDetail.as_view(), name='element-detail'),
]