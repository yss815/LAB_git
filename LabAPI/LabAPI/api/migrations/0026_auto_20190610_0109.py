# Generated by Django 2.2.1 on 2019-06-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20190605_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabPraProbD1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='1')),
                ('prob_body', models.TextField(max_length=2048, null=True)),
                ('prob_option_a', models.CharField(max_length=1024, null=True)),
                ('prob_option_b', models.CharField(max_length=1024, null=True)),
                ('prob_option_c', models.CharField(max_length=1024, null=True)),
                ('prob_option_d', models.CharField(max_length=1024, null=True)),
                ('prob_right', models.CharField(max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='2')),
                ('prob_type', models.CharField(default='多选', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbD2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='2')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_option_a', models.CharField(max_length=1024)),
                ('prob_option_b', models.CharField(max_length=1024)),
                ('prob_option_c', models.CharField(max_length=1024)),
                ('prob_option_d', models.CharField(max_length=1024)),
                ('prob_right', models.CharField(max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='4')),
                ('prob_type', models.CharField(default='多选', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbD3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='3')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_option_a', models.CharField(max_length=1024)),
                ('prob_option_b', models.CharField(max_length=1024)),
                ('prob_option_c', models.CharField(max_length=1024)),
                ('prob_option_d', models.CharField(max_length=1024)),
                ('prob_right', models.CharField(max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='6')),
                ('prob_type', models.CharField(default='多选', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='labpraprob1',
            name='prob_type',
            field=models.CharField(default='单选', max_length=50),
        ),
        migrations.AddField(
            model_name='labpraprob2',
            name='prob_type',
            field=models.CharField(default='单选', max_length=50),
        ),
        migrations.AddField(
            model_name='labpraprob3',
            name='prob_type',
            field=models.CharField(default='单选', max_length=50),
        ),
    ]
