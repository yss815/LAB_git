# Generated by Django 2.2.1 on 2019-06-10 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20190610_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabPraProbK1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='1')),
                ('prob_body', models.TextField(max_length=2048, null=True)),
                ('prob_right', models.CharField(default='在此输入答案', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='1')),
                ('prob_type', models.CharField(default='填空', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbK2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='2')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_right', models.CharField(default='在此输入答案', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='2')),
                ('prob_type', models.CharField(default='填空', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbK3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='3')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_right', models.CharField(default='在此输入答案', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='4')),
                ('prob_type', models.CharField(default='填空', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbP1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='1')),
                ('prob_body', models.TextField(max_length=2048, null=True)),
                ('prob_option_a', models.CharField(max_length=1024, null=True)),
                ('prob_option_b', models.CharField(max_length=1024, null=True)),
                ('prob_option_c', models.CharField(max_length=1024, null=True)),
                ('prob_option_d', models.CharField(max_length=1024, null=True)),
                ('prob_right', models.CharField(default='判断题难度为1', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='1')),
                ('prob_type', models.CharField(default='判断', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbP2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='2')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_option_a', models.CharField(max_length=1024)),
                ('prob_option_b', models.CharField(max_length=1024)),
                ('prob_option_c', models.CharField(max_length=1024)),
                ('prob_option_d', models.CharField(max_length=1024)),
                ('prob_right', models.CharField(default='判断题难度为2', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='2')),
                ('prob_type', models.CharField(default='判断', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LabPraProbP3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_difficult', models.IntegerField(default='3')),
                ('prob_body', models.TextField(max_length=2048)),
                ('prob_option_a', models.CharField(max_length=1024)),
                ('prob_option_b', models.CharField(max_length=1024)),
                ('prob_option_c', models.CharField(max_length=1024)),
                ('prob_option_d', models.CharField(max_length=1024)),
                ('prob_right', models.CharField(default='判断题难度为3', max_length=50, null=True)),
                ('prob_score', models.IntegerField(default='4')),
                ('prob_type', models.CharField(default='判断', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='labpraprobd2',
            name='prob_right',
            field=models.CharField(default='多选题难度为2', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='labpraprobd3',
            name='prob_right',
            field=models.CharField(default='多选题难度为3', max_length=50, null=True),
        ),
    ]