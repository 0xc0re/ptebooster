# Generated by Django 2.1 on 2018-08-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0022_summarizespokentext'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummarizeWrittenText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(max_length=1000)),
                ('model_answer', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]
