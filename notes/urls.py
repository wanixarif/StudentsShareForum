"""textbin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', Posts.as_view(), name='index'),
    path('about/', views.about, name="about"),

    path('materials/', materiallistview.as_view(), name="materials"),
    path('labposts/', labpostlistview.as_view(), name="labposts"),

    path('fullpost/<int:pk>', fullpost.as_view(), name='full_post'),
    path('material/<int:pk>', filefullpost.as_view(), name='material'),

    path('newpost/', PostCreateView.as_view(), name="newpost"),
    path('materialpost/', FilePostCreateView.as_view(), name="materialpost"),


    path("notes/fullpost/<int:pk>/update",
         PostUpdateView.as_view(), name="update"),
    path("notes/material/<int:pk>/update",
         FilePostUpdateView.as_view(), name="material_update"),


    path("notes/fullpost/<int:pk>/delete",
         PostDeleteView.as_view(), name="delete"),
    path("notes/material/<int:pk>/delete",
         FilePostDeleteView.as_view(), name="material_delete"),


    path("user/<str:username>", UserPostListView.as_view(), name="user_posts"),

    path("category/sem/<int:semester>",
         SemesterLabListView.as_view(), name="semester_lab"),
    path("category/branch/<str:branch>",
         BranchLabListView.as_view(), name="branch_lab"),
    path("material/sem/<int:semester>",
         SemesterMaterialListView.as_view(), name="semester_material"),
    path("material/branch/<str:branch>",
         BranchMaterialListView.as_view(), name="branch_material"),

]
