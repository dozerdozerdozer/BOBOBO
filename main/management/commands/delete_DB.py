from django.core.management.base import BaseCommand
from main.models import *


class Command(BaseCommand):
    help = 'Заполнить базу данных тестовыми данными'

    def handle(self, *args, **options):
        Answers.objects.all().delete()
        Questions.objects.all().delete()
        Tags.objects.all().delete()
        User.objects.all().delete()
        QuestionLikes.objects.all().delete()
        AnswerLikes.objects.all().delete()

