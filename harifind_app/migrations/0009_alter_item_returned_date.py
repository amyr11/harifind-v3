# Generated by Django 5.1.4 on 2024-12-15 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harifind_app', '0008_item_returned_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='returned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
