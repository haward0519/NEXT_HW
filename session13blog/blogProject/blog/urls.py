from django.urls import path
from blog import views
from django.contrib import admin

app_name = "blog"
urlpatterns = [
    path('', views.Home, name='Home'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path('new', views.new, name='new'),
    path('list', views.Home, name='list'),
    path('detail/<int:article_id>', views.detail, name='detail'),
    path('list/<str:category_kind>', views.category, name='category'),
    path("comment/<int:article_id>/", views.comment, name="comment"),
    path("delete_comment/<int:article_id>/<int:comment_id>/", views.delete_comment, name="delete_comment"),
    path("all/<int:user_pk>/", views.all, name="all"),

]