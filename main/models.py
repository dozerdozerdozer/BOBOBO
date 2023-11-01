from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')


class Question(models.Model):
    title = models.CharField('Question Title', max_length=100)
    text = models.TextField('Question Text', null=True)
    author = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='questions_written', default=1)
    date_written = models.DateTimeField(null=True)
    tags = models.ManyToManyField('Tags', related_name='questions')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer_text = models.TextField(max_length=1000, default='я дурак')
    likes_amount = models.PositiveIntegerField(default=0)
    truly = models.BooleanField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Tags(models.Model):
    tag_name = models.CharField(max_length=256)
    is_deleted = models.BooleanField(default=False)
