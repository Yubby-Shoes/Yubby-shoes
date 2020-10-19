from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, 'index'),
    path('/about', views.index, 'index'),
]