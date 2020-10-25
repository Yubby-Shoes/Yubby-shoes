from django.urls import path
from .views import Create, List, Detail, Update, Delete, filter_products_bycategory

app_name = 'store'

urlpatterns = [
    # path('', store, name='store'),
    path('create/', Create.as_view(), name="create"),
    path('list/', List.as_view(), name="list"),
    path('filter/<str:category>/', filter_products_bycategory, name="filter"),
    path('detail/<int:pk>/', Detail.as_view(), name="detail"),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
