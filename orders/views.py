from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Order


def clean_old_orders():
    orders = Order.objects.filter(status='Finished')
    for order in orders:
        if order.should_be_removed:
            order.delete()


def order_list(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_order':
            order_number = request.POST['order_number']
            if not Order.objects.filter(order_number=order_number).exists():
                Order.objects.create(order_number=order_number)

        elif action == 'update_order':
            order_id = request.POST['order_id']
            order = get_object_or_404(Order, id=order_id)
            order.mark_as_finished()

        elif action == 'remove_order':
            order_id = request.POST['order_id']
            order = get_object_or_404(Order, id=order_id)
            order.delete()

        return redirect('order_list')

    clean_old_orders()
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    return render(request, 'order_list.html', {
        'in_process_orders': in_process_orders,
        'finished_orders': finished_orders,
    })


def user_order_list(request):
    clean_old_orders()
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    return render(request, 'user_order_list.html', {
        'in_process_orders': in_process_orders,
        'finished_orders': finished_orders,
    })


def get_orders(request):
    clean_old_orders()
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    # Check if request is from monitor display
    is_monitor = 'monitor' in request.path

    if is_monitor:
        # HTML for monitor display
        in_process_html = ''.join([
            f'<div class="order-item in-process">'
            f'<div class="order-number">შეკვეთა: {order.order_number}</div>'
            f'<span class="status-badge status-in-process">მზადდება</span>'
            f'</div>' for order in in_process_orders
        ])
        
        finished_html = ''.join([
            f'<div class="order-item finished">'
            f'<div class="order-number">შეკვეთა: {order.order_number}</div>'
            f'<span class="status-badge status-finished">მზადაა</span>'
            f'</div>' for order in finished_orders
        ])
    else:
        # HTML for order list
        in_process_html = ''.join([
            f'<div class="order-item list-group-item d-flex align-items-center">'
            f'<div class="order-number">'
            f'<i class="bi bi-box-seam me-2"></i>'
            f'შეკვეთა: {order.order_number}'
            f'</div>'
            f'<div class="btn-group ms-auto">'
            f'<button class="btn btn-success btn-sm complete-order" data-id="{order.id}">'
            f'<i class="bi bi-check-circle me-1"></i>დასრულება'
            f'</button>'
            f'<button class="btn btn-danger btn-sm remove-order" data-id="{order.id}">'
            f'<i class="bi bi-trash me-1"></i>წაშლა'
            f'</button>'
            f'</div>'
            f'</div>' for order in in_process_orders
        ])
        
        finished_html = ''.join([
            f'<div class="order-item list-group-item d-flex align-items-center">'
            f'<div class="order-number">'
            f'<i class="bi bi-check-circle me-2"></i>'
            f'შეკვეთა: {order.order_number}'
            f'</div>'
            f'<button class="btn btn-danger btn-sm remove-order ms-auto" data-id="{order.id}">'
            f'<i class="bi bi-trash me-1"></i>წაშლა'
            f'</button>'
            f'</div>' for order in finished_orders
        ])

    return JsonResponse({
        'in_process_html': in_process_html,
        'finished_html': finished_html,
    })


def get_monitor_orders(request):
    """View for monitor display - returns only order numbers and status"""
    clean_old_orders()
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    in_process_html = ''.join([
        f'<div class="order-item in-process">'
        f'<div class="order-number">შეკვეთა: {order.order_number}</div>'
        f'<span class="status-badge status-in-process">მზადდება</span>'
        f'</div>' for order in in_process_orders
    ])
    
    finished_html = ''.join([
        f'<div class="order-item finished">'
        f'<div class="order-number">შეკვეთა: {order.order_number}</div>'
        f'<span class="status-badge status-finished">მზადაა</span>'
        f'</div>' for order in finished_orders
    ])

    return JsonResponse({
        'in_process_html': in_process_html,
        'finished_html': finished_html,
    })


def monitor_display(request):
    """View for monitor display - shows only orders without any UI controls"""
    clean_old_orders()
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    return render(request, 'monitor_display.html', {
        'in_process_orders': in_process_orders,
        'finished_orders': finished_orders,
    })
