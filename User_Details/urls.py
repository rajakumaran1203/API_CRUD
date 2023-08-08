from django.urls import path
from .views import UserRegistrationView, GenerateTokenView, StoreDataView, RetrieveDataView, UpdateDataView, DeleteDataView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('token/', GenerateTokenView.as_view(), name='token'),
    path('data/', StoreDataView.as_view(), name='store-data'),
    path('data/<str:key>/', RetrieveDataView.as_view(), name='retrieve-data'),
    path('data/update/<str:key>/', UpdateDataView.as_view(), name='update-data'),
    path('data/delete/<str:key>/', DeleteDataView.as_view(), name='delete-data'),
]

