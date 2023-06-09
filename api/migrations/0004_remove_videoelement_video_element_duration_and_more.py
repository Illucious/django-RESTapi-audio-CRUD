# Generated by Django 4.2.1 on 2023-05-29 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_videoelement_video_element_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoelement',
            name='video_element_duration',
        ),
        migrations.RemoveField(
            model_name='videoelement',
            name='video_element_upload_time',
        ),
        migrations.AddField(
            model_name='videoelement',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Audio_Element',
            fields=[
                ('audio_element_id', models.AutoField(primary_key=True, serialize=False)),
                ('audio_element_type', models.CharField(choices=[('vo', 'voice-over'), ('bg_music', 'background-music'), ('video_music', 'video-music')], max_length=20)),
                ('high_volume', models.IntegerField()),
                ('low_volume', models.IntegerField()),
                ('url', models.URLField(blank=True, null=True)),
                ('duration', models.JSONField()),
                ('video_element_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.videoelement')),
            ],
        ),
    ]
