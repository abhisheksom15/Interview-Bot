# Generated by Django 2.1.7 on 2019-03-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0007_auto_20190319_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_user',
            name='marks',
            field=models.CharField(max_length=2048),
        ),
    ]
