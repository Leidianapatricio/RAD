from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('eco/<str:texto>/', views.eco, name='eco'),
    path('info/', views.info, name='info'),
]
