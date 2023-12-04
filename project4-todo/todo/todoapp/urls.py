from . import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:t_id>/', views.delete, name='delete'),
    path('cbvdetail/<int:pk>/', views.detail.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.update.as_view(), name='update'),

]
