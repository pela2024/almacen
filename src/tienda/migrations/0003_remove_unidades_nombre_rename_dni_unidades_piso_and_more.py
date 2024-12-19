# Generated by Django 5.1.3 on 2024-12-19 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_consorcio_remove_comision_curso_liquidaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unidades',
            name='Nombre',
        ),
        migrations.RenameField(
            model_name='unidades',
            old_name='Dni',
            new_name='piso',
        ),
        migrations.AddField(
            model_name='unidades',
            name='depto',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255, unique=True)),
                ('consorcio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.consorcio')),
            ],
        ),
        migrations.AddField(
            model_name='unidades',
            name='liquidacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.liquidacion'),
        ),
        migrations.DeleteModel(
            name='Liquidaciones',
        ),
    ]