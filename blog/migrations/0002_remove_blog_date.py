# Generated by Django 3.0.3 on 2020-05-03 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='date',
        ),
    ]
