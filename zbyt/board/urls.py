from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_advert, name="add"),
    path('<int:advert_id>/', views.show_advert, name='show'),
    path('category/<str:cat>/', views.category, name='category'),
    path('type/<str:typ>/', views.by_type, name='type'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
]
