# Generated by Django 2.1 on 2018-08-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0021_auto_20180827_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummarizeSpokenText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(max_length=1000)),
                ('audio', models.FileField(upload_to='ptebooster/media/summarize-spoken-text')),
                ('model_answer', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
