from django.contrib import admin
from django.urls import path, include
from house import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('settings/', views.settings, name="settings"),
    path("user/", views.UserSettingView.as_view(), name="user_setting"),
    # path("signup/", views.signup, name="signup"),
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path('settings/',views.Settings.as_view(), name='settings'),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path('logout/', views.logout_view, name='logout')
]