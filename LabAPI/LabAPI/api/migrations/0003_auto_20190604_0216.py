# Generated by Django 2.2.1 on 2019-06-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190604_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labuserstudent',
            name='student_name',
            field=models.CharField(blank=True, default='', max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='LabGain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain_title', models.CharField(max_length=50)),
                ('gain_decb', models.TextField(blank=True, null=True)),
                ('gain_photo', models.ImageField(blank=True, null=True, upload_to=None)),
                ('gain_see', models.IntegerField(blank=True, null=True)),
                ('belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabUserstudent', to_field='student_name')),
            ],
        ),
    ]