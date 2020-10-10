from django.urls import path
from . import views
urlpatterns = [
    path('thanks/', views.Thanks)
]
