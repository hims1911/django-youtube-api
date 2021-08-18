# Generated by Django 3.2.6 on 2021-08-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=30)),
                ('title', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('channel_id', models.CharField(max_length=30)),
                ('published_at', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail_url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
