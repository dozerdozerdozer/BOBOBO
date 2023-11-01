from django.db import models


class Question(models.Model):
    title = models.CharField('Question Title', max_length=100)
    text = models.TextField('Question Text', null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    question = models.ForeignKey(on_delete=models.CASCADE, to=Question),
    answer_text = models.TextField(max_length=1000),
    profile_pic = models.ImageField(),
    likes_amount = models.PositiveIntegerField(),
    truly = models.BooleanField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
