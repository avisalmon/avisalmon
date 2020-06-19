from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='presenterz'

urlpatterns = [
    path('',
         TemplateView.as_view(template_name='presenterz/presenterz.html'),
         name='presenterz'),
    path('all/', views.LectureListView.as_view(), name='all_lectures'),
]
