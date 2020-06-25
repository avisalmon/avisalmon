from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='presenterz'

urlpatterns = [
    path('',
         TemplateView.as_view(template_name='presenterz/presenterz.html'),
         name='presenterz'),
    path('all/', views.LectureListView.as_view(), name='all_lectures'),
    path('details/<int:pk>',
         views.LectureDetailView.as_view(),
         name='lecture_details'),
    path('create/', views.LectureCreateView.as_view(),
          name='lecture_create'),
    path('update/<int:pk>', views.LectureUpdateView.as_view(),
          name='lecture_update'),
    path('delete/<int:pk>', views.LectureDeleteView.as_view(),
          name='lecture_delete'),
    path('session/create/<int:lecture_pk>',
         views.SessionCreateView.as_view(),
         name='session_create'),
]
