# Generated by Django 4.2.1 on 2023-05-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password1', models.CharField(max_length=65)),
                ('password2', models.CharField(max_length=65)),
                ('codemeli', models.IntegerField(max_length=65)),
                ('number', models.IntegerField(max_length=65)),
            ],
        ),
    ]
