from django.urls import path, re_path
from . import views

app_name='todo'

urlpatterns = [
    path('', views.todo_list_view, name='todo_list_view'),
    path('detail/<int:todo_pk>',
         views.todo_detail_view,
         name='todo_detail_view'),
    path('create/', views.todo_create_view, name='todo_create_view'),
    path('complete/<int:todo_pk>', views.completetodo, name='completetodo'),
    path('completedtodos/', views.completedtodos, name='completedtodos'),
    path('delete/<int:todo_pk>', views.deletetodo, name='deletetodo',)

]
