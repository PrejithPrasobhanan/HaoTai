from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name = "home"),
    path('about/', views.about,name = "about"),
    path('jobs/<int:id>', views.jobs,name = "jobs"),
    path('jobs', views.jobs,name = "jobss"),
    path('benefits/<int:id>', views.benefits,name = "benefits"),
]