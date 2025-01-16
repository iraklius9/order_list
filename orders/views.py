from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order


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
            order.status = 'Finished'
            order.save()

            finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')
            if finished_orders.count() > 10:
                finished_orders.last().delete()

        elif action == 'remove_order':
            order_id = request.POST['order_id']
            order = get_object_or_404(Order, id=order_id)
            order.delete()

        return redirect('order_list')

    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    return render(request, 'order_list.html', {
        'in_process_orders': in_process_orders,
        'finished_orders': finished_orders,
    })


def user_order_list(request):
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    return render(request, 'user_order_list.html', {
        'in_process_orders': in_process_orders,
        'finished_orders': finished_orders,
    })


def get_orders(request):
    in_process_orders = Order.objects.filter(status='In Process').order_by('-created_at')
    finished_orders = Order.objects.filter(status='Finished').order_by('-created_at')

    in_process_html = ''.join(
        [f'<li class="list-group-item"><strong>შეკვეთა:</strong> {order.order_number}</li>' for order in
         in_process_orders])
    finished_html = ''.join([
                                f'<li class="list-group-item"><strong>შეკვეთა:</strong> {order.order_number} <span class="text-muted">მზადაა</span></li>'
                                for order in finished_orders])

    return JsonResponse({
        'in_process_html': in_process_html,
        'finished_html': finished_html,
    })
