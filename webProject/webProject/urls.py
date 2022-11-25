from django.contrib import admin
from django.urls import path, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('error/', views.error),
    re_path(r"^user/(?P<name>\D+)/(?P<name_folder>\D+)/(?P<num_post>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)/(?P<name_folder>\D+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user)
]
