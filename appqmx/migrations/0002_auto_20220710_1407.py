# Generated by Django 3.2.14 on 2022-07-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appqmx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbxt',
            name='stc_CbjH',
            field=models.CharField(max_length=32, null=True, verbose_name='机号'),
        ),
        migrations.AddField(
            model_name='cbxt',
            name='stc_CbxH',
            field=models.CharField(max_length=32, null=True, verbose_name='型号'),
        ),
    ]