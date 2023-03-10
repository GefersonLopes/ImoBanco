# Generated by Django 4.1.7 on 2023-02-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
