# Generated by Django 2.1.7 on 2019-03-19 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Front', '0006_auto_20190319_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_marks',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Front.result_user'),
        ),
    ]