# Generated by Django 4.1.1 on 2022-09-15 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_alter_articletype_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articletype',
            name='articles',
        ),
    ]