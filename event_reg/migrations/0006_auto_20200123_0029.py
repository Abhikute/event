# Generated by Django 2.2.2 on 2020-01-22 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0005_temp_images_temp_videos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temp_videos',
            old_name='image',
            new_name='video',
        ),
    ]
