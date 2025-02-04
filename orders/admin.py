from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'created_at', 'finished_at')
    list_filter = ('status',)
    search_fields = ('order_number',)
    ordering = ('-created_at',)
