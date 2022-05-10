# Generated by Django 4.0.4 on 2022-05-10 19:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_meal_lat_alter_meal_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='invitee_names',
            field=models.ManyToManyField(blank=True, related_name='invitee_names', to=settings.AUTH_USER_MODEL),
        ),
    ]
