# Generated by Django 2.2.1 on 2019-06-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190610_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
