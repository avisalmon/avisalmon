from django.urls import path
from . import views

app_name='portfolio'

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('details/<int:project_id>',
         views.project_details,
         name='project_details'),
]
