# Generated by Django 4.0.4 on 2022-05-04 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_meal_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='archive',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
