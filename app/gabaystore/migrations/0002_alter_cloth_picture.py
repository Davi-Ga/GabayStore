# Generated by Django 3.2.13 on 2022-07-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gabaystore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='picture',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
