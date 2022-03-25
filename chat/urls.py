
from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('<str:group_id>/', views.room, name='room'),
]
