# Generated by Django 2.2.2 on 2019-12-08 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0005_auto_20191208_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='user',
        ),
    ]
