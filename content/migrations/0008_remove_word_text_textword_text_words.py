# Generated by Django 4.1.3 on 2022-12-01 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0007_word_text"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="word",
            name="text",
        ),
        migrations.CreateModel(
            name="TextWord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "text",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="content.text"
                    ),
                ),
                (
                    "word",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="content.word"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="text",
            name="words",
            field=models.ManyToManyField(through="content.TextWord", to="content.word"),
        ),
    ]