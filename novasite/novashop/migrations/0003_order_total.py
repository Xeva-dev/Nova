# Generated by Django 4.2 on 2025-02-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novashop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
