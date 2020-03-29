from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.add_advert, name="add"),
    path('<int:advert_id>/', views.show_advert, name='show'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
]