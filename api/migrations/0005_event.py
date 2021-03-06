# Generated by Django 3.0.14 on 2021-08-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210820_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('photo', models.ImageField(max_length=1000, upload_to='')),
                ('button', models.CharField(max_length=100)),
            ],
        ),
    ]
