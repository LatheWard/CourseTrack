# Generated by Django 3.2 on 2021-04-30 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergrade',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='grade', to=settings.AUTH_USER_MODEL),
        ),
    ]