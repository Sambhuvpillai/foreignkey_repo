# Generated by Django 4.0.4 on 2022-04-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
