# Generated by Django 2.2.1 on 2019-06-05 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190605_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabPraPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paper_difficult', models.IntegerField(default='1')),
                ('paper_d1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabPraProb1')),
                ('paper_d2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabPraProb2')),
                ('paper_d3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.LabPraProb3')),
            ],
        ),
    ]
