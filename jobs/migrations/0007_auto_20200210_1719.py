# Generated by Django 3.0.2 on 2020-02-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20200210_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='juego',
            name='jugador',
            field=models.ManyToManyField(null=True, to='jobs.Jugador'),
        ),
    ]
