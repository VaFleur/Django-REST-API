# Generated by Django 4.1.1 on 2022-09-15 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_articletype_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='articletype',
            options={'ordering': ['name']},
        ),
    ]
