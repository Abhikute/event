# Generated by Django 2.2.2 on 2019-12-08 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='user_register',
        ),
    ]
