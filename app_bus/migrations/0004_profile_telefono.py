# Generated by Django 2.1 on 2020-02-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bus', '0003_auto_20200215_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telefono',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
