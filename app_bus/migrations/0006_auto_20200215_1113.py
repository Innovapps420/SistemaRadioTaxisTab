# Generated by Django 2.1 on 2020-02-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_bus', '0005_profile_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruta',
            name='calificacion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ruta',
            name='estatus',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
