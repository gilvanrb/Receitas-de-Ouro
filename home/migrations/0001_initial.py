# Generated by Django 5.2 on 2025-04-16 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('descricão', models.TextField(max_length=150)),
                ('ingredientes', models.TimeField()),
                ('preparo', models.TextField()),
            ],
        ),
    ]
