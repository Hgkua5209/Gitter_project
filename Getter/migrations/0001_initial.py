# Generated by Django 4.1.4 on 2023-02-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('studentName', models.CharField(max_length=128)),
                ('studentPhone', models.CharField(max_length=128)),
            ],
        ),
    ]
