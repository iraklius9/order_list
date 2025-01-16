from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Admin page
    path('user/', views.user_order_list, name='user_order_list'),  # User page without buttons
    path('get_orders/', views.get_orders, name='get_orders'),  # AJAX endpoint
]
