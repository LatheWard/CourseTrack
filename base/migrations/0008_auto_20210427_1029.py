# Generated by Django 3.1.4 on 2021-04-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20210427_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.TextField(default=None, max_length=40),
        ),
    ]