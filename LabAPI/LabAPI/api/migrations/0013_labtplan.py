# Generated by Django 2.2.1 on 2019-06-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_delete_labsplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_ID', models.ForeignKey(on_delete='CASCADE', to='api.LabPlan')),
                ('user_ID', models.ForeignKey(on_delete='CASCADE', to='api.LabUserstudent')),
            ],
        ),
    ]