# Generated by Django 3.2 on 2022-07-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20220709_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='producto/%Y/%m/%d'),
        ),
    ]
