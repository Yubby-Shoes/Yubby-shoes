from django.urls import path
from .views import (Create, Detail, Update, Delete,
                    filter_products_bycategory, Orders, OrderStatusUpdateView, customers_view, customers_update)

app_name = 'store'
# store/
urlpatterns = [
    # path('', store, name='store'),
    path('create/', Create.as_view(), name="create"),
    # path('list/', List.as_view(), name="list"),
    path('filter/<str:category>/', filter_products_bycategory, name="filter"),
    path('detail/<int:pk>/', Detail.as_view(), name="detail"),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('orders/', Orders.as_view(), name='orders'),
    path('customers/', customers_view, name='customers'),
    path('orders/<int:pk>/update/', OrderStatusUpdateView.as_view(),
         name='order-status-update'),
    path('customers/update/<int:pk>/', customers_update,
         name='customers_update'),
]
