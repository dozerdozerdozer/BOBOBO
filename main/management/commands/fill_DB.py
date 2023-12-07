from django.core.management.base import BaseCommand
from main.models import Questions, Answers, User, Tags
import random


class Command(BaseCommand):
    help = 'Заполнить базу данных тестовыми данными'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Количество ячеек для заполнения')

    def handle(self, *args, **options):
        ratio = options['ratio']

        users_data_to_insert = []
        questions_data_to_insert = []
        answers_data_to_insert = []
        tags_data_to_insert = []

        Answers.objects.all().delete()
        Questions.objects.all().delete()
        Tags.objects.all().delete()
        User.objects.all().delete()

        for i in range(ratio):
            print('Tag ', i)
            tag_data = Tags(
                tag_name=f'Tag №{i+1}',
                count_of_questions=10)
            tags_data_to_insert.append(tag_data)

        Tags.objects.bulk_create(tags_data_to_insert)

        for i in range(ratio):
            print('User ', i)
            user_data = User(
                nickname=f'User_{i+1}',
                password=f'User_{i+1}_password',
                username=f'User_{i+1}')
            users_data_to_insert.append(user_data)

        User.objects.bulk_create(users_data_to_insert)

        for i in range(ratio * 10):
            print('Que ', i)
            question_data = Questions.objects.create(
                title=f'How to be a num {i + 1}?',
                text=f'Этот вопрос принадлежит пользователю User_{i // 10}, добавлен на сайт {i + 1}-м по очереди.',
                author=User.objects.get(username=f'User_{(i // 10) + 1}'),
                amount_of_likes=random.randint(0, 1000),
                amount_of_answers=10)

            tags = [
                Tags.objects.get(tag_name=f'Tag №{random.randint(1, ratio)}'),
                Tags.objects.get(tag_name=f'Tag №{random.randint(1, ratio)}'),
            ]

            question_data.tags.set(tags)
            questions_data_to_insert.append(question_data)

        for i in range(ratio * 100):
            k = random.randint(0, ratio-1)
            answer_data = Answers(
                question=Questions.objects.get(title=f'How to be a num {(i // 10) + 1}?'),
                answer_text=f'Этот ответ принадлежит пользователю User_{k+1}',
                author=User.objects.get(username=f'User_{k+1}'),
                amount_of_likes=random.randint(0, 1000))
            answers_data_to_insert.append(answer_data)
            print('Answer ', i)

        Answers.objects.bulk_create(answers_data_to_insert)

        self.stdout.write(self.style.SUCCESS(f'Добавлено {ratio} записей в базу данных.'))
