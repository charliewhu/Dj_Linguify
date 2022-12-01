# Generated by Django 4.1.3 on 2022-12-01 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0006_alter_word_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="word",
            name="text",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="content.text",
            ),
        ),
    ]