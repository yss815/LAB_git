# Generated by Django 2.2.1 on 2019-06-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_labpracresult_labpraprob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labpraprob',
            name='prob_date',
        ),
        migrations.AddField(
            model_name='labpraprob',
            name='prob_score',
            field=models.IntegerField(default='2'),
        ),
    ]