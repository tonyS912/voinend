from django.contrib import admin
from django.urls import path

from authentication.views import LoginView, RegisterView
from contacts.views import ContactView, ContactDetailView
from tasks.views import TasksView, TasksDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('contact/', ContactView.as_view()),
    path('contact/<int:id>/', ContactDetailView.as_view()),
    path('tasks/', TasksView.as_view()),
    path('tasks/<int:id>/', TasksDetailView.as_view()),
]
