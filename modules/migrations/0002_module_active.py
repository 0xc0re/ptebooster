# Generated by Django 2.1 on 2018-08-14 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
