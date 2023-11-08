# Generated by Django 4.2.6 on 2023-11-08 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0006_questions_amount_of_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='main.users'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions_written', to='main.users'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='main.tags'),
        ),
        migrations.AlterField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission'),
        ),
    ]
