# Generated by Django 3.2.23 on 2024-02-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dos', '0005_rename_request_request_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pin',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
