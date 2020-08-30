# Generated by Django 3.1 on 2020-08-28 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='idtipodocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.tipodocumento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='lugarresidencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.ciudad'),
        ),
    ]
