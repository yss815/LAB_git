# Generated by Django 2.2.1 on 2019-06-10 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20190610_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labregister',
            options={'ordering': ['date_time']},
        ),
    ]