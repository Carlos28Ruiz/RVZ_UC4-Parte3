# Generated by Django 4.0.5 on 2022-07-27 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=150)),
                ('apepat', models.CharField(max_length=150)),
                ('apemat', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=300)),
                ('telefono', models.IntegerField()),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
    ]
