# Generated by Django 3.1.7 on 2021-04-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='username',
            field=models.CharField(default='', max_length=100),
        ),
    ]
