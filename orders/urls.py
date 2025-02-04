from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),  # Admin page
    path('user/', views.user_order_list, name='user_order_list'),  # User page without buttons
    path('get_orders/', views.get_orders, name='get_orders'),  # AJAX endpoint
    path('monitor/', views.monitor_display, name='monitor_display'),
    path('get_monitor_orders/', views.get_monitor_orders, name='get_monitor_orders'),  # Monitor AJAX endpoint
]
