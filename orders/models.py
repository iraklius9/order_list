from django.db import models
from django.utils import timezone
from datetime import timedelta

class Order(models.Model):
    order_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='In Process')
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def mark_as_finished(self):
        self.status = 'Finished'
        self.finished_at = timezone.now()
        self.save()

    @property
    def should_be_removed(self):
        if self.status == 'Finished' and self.finished_at:
            return timezone.now() > self.finished_at + timedelta(minutes=10)
        return False
