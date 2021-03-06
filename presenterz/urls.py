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
    path('session/<int:pk>',
         views.SessionDetailView.as_view(),
         name='session_details'),
    path('session/update/<int:pk>',
         views.SessionUpdateView.as_view(),
         name='session_update'),
    path('session/delete/<int:pk>',
         views.SessionDeleteView.as_view(),
         name='session_delete'),
    path('participation/create/<int:session_pk>',
         views.partcipationCreate,
         name='participation_create'),
    path('participation/delete/<int:session_pk>',
         views.paticipationDelete,
         name='participation_delete'),
]
