# Generated by Django 5.0.3 on 2024-05-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0023_alter_appuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='visits',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
