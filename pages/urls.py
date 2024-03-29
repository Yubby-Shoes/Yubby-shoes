from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop/women', views.shop_women, name='shop_women'),
    path('shop/item/<int:pk>', views.item_detail, name='item_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/item/<int:pk>/buy', views.buy, name='buy'),
]
