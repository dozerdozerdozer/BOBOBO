from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from django.core.paginator import Paginator


def paginate(objects, page, per_page = 10):
    paginator = Paginator(objects, per_page)
    return paginator.page(page)


def index(request):
    page = int(request.GET.get('page', 1))
    return render(request, 'main/index.html', {'title': 'Home Page', 'questions': paginate(Question, page)})


def question(request, question_id):
    items = Question[question_id]
    return render(request, 'main/question.html', {'questions': items})


def profile(request):
    return render(request, 'main/profile.html')


def login(request):
    return render(request, 'main/login.html')


def registration(request):
    return render(request, 'main/registration.html')


def ask(request):
    error = ''
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Wrong form!'

    form = QuestionForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/ask.html', context)




