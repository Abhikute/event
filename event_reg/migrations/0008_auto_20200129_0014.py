# Generated by Django 2.2.2 on 2020-01-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0007_auto_20200123_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_instructuions',
        ),
        migrations.AddField(
            model_name='event',
            name='Registration_fees_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='entry_deadline_instruction',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='file_categories_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='file_size_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='file_type_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='notification_date_instruction',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='other_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='participant_Age_instruction',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='prize_dist_instruction',
            field=models.DateField(null=True),
        ),
    ]
