# Generated by Django 4.2.6 on 2023-11-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_answers_author_alter_questions_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='amount_of_answers',
            field=models.IntegerField(default=0, verbose_name='Answers'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='truly',
            field=models.BooleanField(default=False),
        ),
    ]
