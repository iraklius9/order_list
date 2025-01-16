from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[('In Process', 'In Process'), ('Finished', 'Finished')],
        default='In Process'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_number} - {self.status}"
