# Generated by Django 4.1.3 on 2022-11-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0004_word"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="status",
            field=models.CharField(default="New", max_length=10),
        ),
    ]
