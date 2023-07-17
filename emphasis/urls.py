from django.urls import path
from . import views

app_name = "emphasis"

urlpatterns = [
    path('', views.index, name="index"),
    path('words/', views.words, name="words"),
    path('play/', views.play, name="play"),
    path('mistakes/', views.mistakes, name="mistakes"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('profile/<str:username>', views.profile, name="profile"),
]
