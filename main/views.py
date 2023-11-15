from django.shortcuts import render
from .services import *


def base_context(request):
    best_users = Users.objects.all().order_by('-correct_answers_amount')[:5]
    tags = Tags.objects.all().order_by('count_of_questions')[:10]
    return {'best_users': best_users, 'tags': tags}


def error_404_view(request, exception):
    return render(request, 'main/404.html')


def error_500_view(request):
    return render(request, 'main/500.html')


def index(request):
    return render(request, 'main/index.html', index_context(request))


def tag(request, tag_id=20000):
    return render(request, 'main/index.html', tag_context(request, tag_id))


def hot(request):
    return render(request, 'main/index.html', hot_context(request))


def question(request, question_id):
    return render(request, 'main/question.html', question_context(request, question_id))


def profile(request):
    return render(request, 'main/profile.html')


def login(request):
    return render(request, 'main/login.html')


def registration(request):
    return render(request, 'main/registration.html')


def ask(request):
    return render(request, 'main/ask.html')







