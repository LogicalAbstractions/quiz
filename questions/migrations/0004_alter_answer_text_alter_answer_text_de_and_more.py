# Generated by Django 4.1.4 on 2022-12-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0003_question_explanation_question_explanation_de_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="text",
            field=models.TextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name="answer",
            name="text_de",
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name="answer",
            name="text_en",
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name="fact",
            name="text",
            field=models.TextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name="question",
            name="explanation",
            field=models.TextField(
                blank=True, default=None, max_length=4096, null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="explanation_de",
            field=models.TextField(
                blank=True, default=None, max_length=4096, null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="explanation_en",
            field=models.TextField(
                blank=True, default=None, max_length=4096, null=True
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="text",
            field=models.TextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name="question",
            name="text_de",
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="text_en",
            field=models.TextField(max_length=4096, null=True),
        ),
    ]
