# Generated by Django 3.2 on 2022-10-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mocked', '0002_auto_20180815_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
