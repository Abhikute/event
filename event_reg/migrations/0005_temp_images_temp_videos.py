# Generated by Django 2.2.2 on 2020-01-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_reg', '0004_paytmhistory_user_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_reg_id', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_reg_id', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
            ],
        ),
    ]
