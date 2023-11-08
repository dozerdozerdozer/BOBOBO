# Generated by Django 4.2.6 on 2023-11-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_answers_is_correct_users_correct_answers_amount_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Questions',
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AddField(
            model_name='tags',
            name='count_of_questions',
            field=models.IntegerField(default=0),
        ),
    ]
