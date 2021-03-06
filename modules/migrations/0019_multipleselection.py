# Generated by Django 2.1 on 2018-08-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0018_reorderparagraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(blank=True, upload_to='ptebooster/media/multiple-selection-listening')),
                ('paragraph', models.TextField(blank=True, max_length=600)),
                ('option_1', models.CharField(max_length=150)),
                ('option_2', models.CharField(max_length=150)),
                ('option_3', models.CharField(max_length=150)),
                ('option_4', models.CharField(max_length=150)),
                ('option_5', models.CharField(blank=True, max_length=150)),
                ('option_6', models.CharField(blank=True, max_length=150)),
                ('answers', models.CharField(max_length=150)),
            ],
        ),
    ]
