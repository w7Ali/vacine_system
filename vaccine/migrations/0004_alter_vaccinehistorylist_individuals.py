# Generated by Django 3.2.12 on 2022-02-18 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0003_auto_20220217_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinehistorylist',
            name='individuals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vaccine.individuallist'),
        ),
    ]
