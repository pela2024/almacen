from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('tienda', '0009_alter_gastos_options_remove_gastos_rubro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=255, verbose_name='Razón Social')),
                ('cuit', models.CharField(max_length=11, unique=True, verbose_name='CUIT')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
        ),
        migrations.AddField(
            model_name='consorcio',
            name='administracion',
            field=models.ForeignKey(
                null=True,  # Permite valores nulos para migración
                on_delete=django.db.models.deletion.CASCADE, 
                related_name='consorcios', 
                to='tienda.Administracion'
            ),
        ),
    ]
