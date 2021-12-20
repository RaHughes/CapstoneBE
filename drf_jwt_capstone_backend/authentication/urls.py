from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, GetUser, GetBusiness, GetMessage

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', GetUser.as_view(), name='user'),
    path('business/<int:pk>', GetBusiness.as_view(), name='business'),
    path('business/', GetBusiness.as_view(), name='business'),
    path('message/', GetMessage.as_view(), name='message')
]
