from django.urls import path
from . import views

app_name='randg'

urlpatterns = [
    path('', views.randg, name='randg'),
    path('generate/', views.generate, name='generate'),
]
