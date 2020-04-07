from django.urls import path
from .views import CustomerCreate,CustomerList,CustomerDetails,UserList
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [


path('users/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('customer/create/', CustomerCreate.as_view(),name='customer_create'),
path('customer/list/', CustomerList.as_view(),name='customer_list'),
path('customer/<int:pk>/', CustomerDetails.as_view(),name='customer_updateDelete'),
path('customer/users/', UserList.as_view()),

]
