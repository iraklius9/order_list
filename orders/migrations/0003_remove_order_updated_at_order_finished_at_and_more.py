# Generated by Django 5.1.5 on 2025-02-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_item_name_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='order',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='In Process', max_length=20),
        ),
    ]
