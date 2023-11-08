import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)
    correct_answers_amount = models.IntegerField(default=0)
    nickname = models.CharField('User Nickname', max_length=50, default='durachyo')


class Questions(models.Model):
    title = models.CharField('Question Title', max_length=100)
    text = models.TextField('Question Text', null=True)
    author = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='questions_written')
    date_written = models.DateTimeField(default=datetime.datetime.now)
    tags = models.ManyToManyField('Tags', related_name='questions')
    is_deleted = models.BooleanField(default=False)
    amount_of_likes = models.PositiveIntegerField('Likes', default=0)
    amount_of_answers = models.PositiveIntegerField('Answers', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, default=None)
    answer_text = models.TextField(max_length=1000, default='я дурак')
    likes_amount = models.PositiveIntegerField(default=0)
    truly = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey(Users, on_delete=models.PROTECT, default='')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Tags(models.Model):
    tag_name = models.CharField(max_length=256)
    is_deleted = models.BooleanField(default=False)
    count_of_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
