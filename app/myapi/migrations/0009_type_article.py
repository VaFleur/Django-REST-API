# Generated by Django 4.1.1 on 2022-09-15 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_type_delete_articletype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.article'),
        ),
    ]
