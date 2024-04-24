# Generated by Django 5.0.3 on 2024-04-24 03:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=100)),
                ('biography', models.TextField(blank=True)),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(blank=True, to='Music.genre')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('cover_art', models.ImageField(blank=True, upload_to='playlist_covers/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.artist')),
                ('genres', models.ManyToManyField(blank=True, to='Music.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('cover_art', models.ImageField(upload_to='album_covers/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.artist')),
                ('genres', models.ManyToManyField(blank=True, to='Music.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('audio_file', models.FileField(upload_to='tracks/')),
                ('duration', models.DurationField()),
                ('plays', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.artist')),
                ('genre', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Music.genre')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_order', models.PositiveIntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.extendedplaylist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.track')),
            ],
        ),
        migrations.AddField(
            model_name='extendedplaylist',
            name='tracks',
            field=models.ManyToManyField(blank=True, to='Music.track'),
        ),
        migrations.CreateModel(
            name='AlbumTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.album')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Music.track')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(blank=True, to='Music.track'),
        ),
    ]
