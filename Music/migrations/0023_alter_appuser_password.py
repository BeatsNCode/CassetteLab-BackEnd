# Generated by Django 5.0.3 on 2024-05-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0022_alter_appuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
