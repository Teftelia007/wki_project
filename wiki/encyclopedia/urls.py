from django.urls import path

from . import views
from . import util
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_title, name = "get_title"),
    path("search", views.search, name= "search"),
    path("wiki/create page/new page", views.create_page, name = "create_page"),
    path("edit/<str:title>",views.edit_title, name = "edit_title"),
    path("wiki/my/random_page",views.random_page, name = "random_page")
]