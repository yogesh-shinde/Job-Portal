# Generated by Django 3.0 on 2019-12-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
        ('FirstApp', '0004_auto_20191216_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='civiljobs',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.User'),
        ),
        migrations.AddField(
            model_name='itjobs',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.User'),
        ),
        migrations.AddField(
            model_name='mechjobs',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.User'),
        ),
    ]
