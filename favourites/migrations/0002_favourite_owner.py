# Generated by Django 3.0.7 on 2020-06-07 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favourite',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]