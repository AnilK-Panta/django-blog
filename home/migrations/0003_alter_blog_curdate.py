# Generated by Django 4.0.1 on 2022-02-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='curdate',
            field=models.DateField(),
        ),
    ]
