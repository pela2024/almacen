# Generated by Django 5.1.3 on 2025-02-01 15:55

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(blank=True, max_length=150, null=True)),
                ('cuit', models.CharField(max_length=11, unique=True)),
                ('rubro', models.CharField(blank=True, max_length=100, null=True)),
                ('actividad', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consorcio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_del_consorcio', models.CharField(max_length=255, verbose_name='Clave del Consorcio')),
                ('cuit', models.CharField(max_length=11, unique=True, verbose_name='CUIT')),
                ('direccion', models.CharField(max_length=255, verbose_name='Dirección')),
                ('administracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consorcios', to='tienda.administracion')),
            ],
        ),
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(max_length=255)),
                ('consorcio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.consorcio')),
            ],
            options={
                'unique_together': {('consorcio', 'periodo')},
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobante', models.CharField(max_length=22)),
                ('concepto', models.CharField(max_length=1000)),
                ('a', models.CharField(max_length=150)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rubro', models.IntegerField()),
                ('consorcio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to='tienda.consorcio')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gastos', to='tienda.proveedor')),
            ],
            options={
                'verbose_name': 'gasto',
                'verbose_name_plural': 'gastos',
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.IntegerField()),
                ('depto', models.CharField(max_length=255)),
                ('liquidacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.liquidacion')),
            ],
            options={
                'verbose_name': 'unidad',
                'verbose_name_plural': 'unidades',
                'unique_together': {('liquidacion', 'piso')},
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('unidad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.unidades')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('consorcio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuarios', to='tienda.consorcio')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='usuario_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
