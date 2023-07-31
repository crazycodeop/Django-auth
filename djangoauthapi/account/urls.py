from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePassView, SendPassResetEmail, PasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('change-pass/', UserChangePassView.as_view(), name='changepass'),
    path('reset-pass/', SendPassResetEmail.as_view(), name='resetpass-email'),
    path('reset-pass/<uid>/<token>/', PasswordResetView.as_view(), name='reset'),
]