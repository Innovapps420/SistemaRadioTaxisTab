# Generated by Django 2.1 on 2020-02-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bus', '0006_auto_20200215_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='apellidos',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nombre',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]