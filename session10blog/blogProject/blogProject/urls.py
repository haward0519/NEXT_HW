"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('new', views.new, name='new'),
    path('list', views.Home, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('list/<str:category_kind>', views.category, name='category'),
    path("comment/<int:article_id>/", views.comment, name="comment"),
    path("delete_comment/<int:article_id>/<int:comment_id>/", views.delete_comment, name="delete_comment"),
    path("recomment/<int:article_id>/<int:comment_id>/", views.recomment, name="recomment"),
    path("recomment_delete/<int:article_id>/<int:comment_id>/<int:recomment_id>/", views.recomment_delete, name="recomment_delete"),
]
