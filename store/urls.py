from django.urls import path
from .views import Create, List, Detail, Update, Delete

app_name = 'store'

urlpatterns = [
    # path('', store, name='store'),
    path('create/', Create.as_view(), name="create"),
    path('list/', List.as_view(), name="list"),
    path('detail/<int:pk>/', Detail.as_view(), name="detail"),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
