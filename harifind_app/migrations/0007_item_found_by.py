# Generated by Django 5.1.4 on 2024-12-15 05:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harifind_app', '0006_subscription_active_subscription_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='found_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='found_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
