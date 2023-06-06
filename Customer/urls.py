from django.urls import path
from .views import Index, Order

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('order/', Order.as_view(), name="order"),   
]
