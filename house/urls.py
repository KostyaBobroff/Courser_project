from django.contrib import admin
from django.urls import path, include
from house import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('settings/', views.settings, name="settings"),
    path("user/", views.user_settings, name="user_setting"),
    path("signup/", views.signup, name="signup"),
    path('settings/',views.Settings.as_view(), name='settings'),
]