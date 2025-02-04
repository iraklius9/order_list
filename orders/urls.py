from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', views.order_list, name='order_list'),
    path('user-orders/', views.user_order_list, name='user_order_list'),
    path('monitor/', views.monitor_display, name='monitor_display'),
    path('get-orders/', views.get_orders, name='get_orders'),
    path('monitor-orders/', views.get_monitor_orders, name='monitor_orders'),
    path('mark-as-finished/<str:order_number>/', views.mark_as_finished, name='mark_as_finished'),
]
