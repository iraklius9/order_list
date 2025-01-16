# Generated by Django 5.1.4 on 2025-01-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In Process', 'In Process'), ('Finished', 'Finished')], default='In Process', max_length=20),
        ),
    ]
