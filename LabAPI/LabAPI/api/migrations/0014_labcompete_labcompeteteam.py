# Generated by Django 2.2.1 on 2019-06-04 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_labtplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabCompete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compete_name', models.CharField(max_length=50)),
                ('compete_desc', models.CharField(max_length=50)),
                ('compete_type', models.CharField(max_length=20)),
                ('compete_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LabCompeteTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_compete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabCompete')),
                ('team_playerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabUserstudent')),
            ],
        ),
    ]
