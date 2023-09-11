from django.contrib import admin
from django.urls import path, include

from authentication.views import LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
