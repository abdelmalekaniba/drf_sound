# Generated by Django 4.1.7 on 2023-03-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children_sounds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sound',
            name='name',
            field=models.FileField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='sound',
            name='sound',
            field=models.FileField(upload_to='sound/'),
        ),
    ]
