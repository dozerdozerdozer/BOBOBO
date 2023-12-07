import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле Email должно быть заполнено')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    def best_users(self, amount):
        return self.all().order_by('-correct_answers_amount')[:amount]


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True, default="css_ava.jpg", upload_to="avatar/%Y/%m/%d")
    correct_answers_amount = models.IntegerField(default=0)
    nickname = models.CharField('User Nickname', max_length=50, default='user')
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    objects = UserManager()


class QuestionsManager(models.Manager):

    def all_best_questions(self):
        return self.all().order_by('amount_of_likes')

    def few_best_questions(self, amount):
        return self.all().order_by('amount_of_likes')[:amount]

    def hot_questions(self):
        return self.all().order_by('amount_of_answers')

    def this_tag_questions(self, tag_id):
        tag = Tags.objects.get(id=tag_id)
        return self.get_queryset().filter(tags=tag).order_by('-id')


class Questions(models.Model):
    title = models.CharField('Question Title', max_length=100)
    text = models.TextField('Question Text', null=False, default="Im idiot!")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='questions_written')
    date_written = models.DateTimeField(default=datetime.datetime.now)
    tags = models.ManyToManyField('Tags', related_name='questions')
    is_deleted = models.BooleanField(default=False)
    amount_of_likes = models.PositiveIntegerField('Likes', default=0)
    amount_of_answers = models.PositiveIntegerField('Answers', default=0)

    objects = QuestionsManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class AnswersManager(models.Manager):
    def this_questions_answers(self, question_id):
        return self.all().filter(question=question_id)


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, default=None)
    answer_text = models.TextField(max_length=1000, default='i dont understand u friend')
    amount_of_likes = models.PositiveIntegerField('Likes', default=0)
    date_written = models.DateTimeField(default=datetime.datetime.now)
    truly = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default='')

    objects = AnswersManager()

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self, page_number):
        question_url = reverse('question', args=[str(self.question.id)])
        return f"{question_url}?page={page_number}#{self.id}"

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class TagsManager(models.Manager):
    def best_tags(self):
        return self.all().order_by('-count_of_questions')

    def few_best_tags(self, amount):
        return self.all().order_by('-count_of_questions')[:amount]


class Tags(models.Model):
    tag_name = models.CharField(max_length=256)
    is_deleted = models.BooleanField(default=False)
    count_of_questions = models.IntegerField(default=0)

    objects = TagsManager()

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class QuestionLikes(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    type = models.BooleanField(default=True)

    class Meta:
        unique_together = ['question', 'author']

    def __str__(self):
        return f'Like from user: {self.author}, to {Questions.objects.get(id=self.question)}'


class AnswerLikes(models.Model):
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    type = models.BooleanField(default=True)

    class Meta:
        unique_together = ['answer', 'author']

    def __str__(self):
        return f'Like from user: {self.author}, to {Answers.objects.get(id=self.answer)}'
