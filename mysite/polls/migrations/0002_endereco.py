# Generated by Django 3.2.20 on 2023-07-04 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=59)),
            ],
        ),
    ]
