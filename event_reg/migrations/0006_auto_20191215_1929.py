# Generated by Django 2.2.2 on 2019-12-15 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0005_auto_20191215_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='user_registration',
            new_name='user_reg',
        ),
    ]
