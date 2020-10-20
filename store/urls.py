from django.urls import path
from .views import Create, List

app_name = 'store'

urlpatterns = [
    # path('', store, name='store'),
    path('create/', Create.as_view(), name="create"),
    path('list/', List.as_view(), name="list")
]
