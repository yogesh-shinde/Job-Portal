# Generated by Django 3.0 on 2019-12-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civiljobs',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='itjobs',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mechjobs',
            name='job_description',
            field=models.TextField(),
        ),
    ]
