from django.shortcuts import render, redirect
from .models import Questions, Users, Tags, Answers
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def base_context(request):
    best_users = Users.objects.all().order_by('-correct_answers_amount')[:5]
    tags = Tags.objects.all().order_by('count_of_questions')[:10]
    return {'best_users': best_users, 'tags': tags}


def paginate(objects, page=1, per_page=20):
    # page - номер страницы, которую нужно отобразить (по умолчанию 1)
    # per_page - кол-во элементов на странице *по умолчанию 10)

    paginator = Paginator(objects, per_page)
    try:
        que = paginator.page(page)
    except PageNotAnInteger:
        que = paginator.page(1)
    except EmptyPage:
        que = paginator.page(paginator.num_pages)
    return que


def index(request, tag_id=None, page=1):
    if tag_id:
        try:
            tag = Tags.objects.get(id=tag_id)
        except:
            tag = Tags.objects.get(id=1)

        questions = Questions.objects.filter(tags=tag).order_by('-id')
    else:
        questions = Questions.objects.all().order_by('-id')
    context = {
        'title': 'Home Page',
        'questions': paginate(questions, page),
    }
    return render(request, 'main/index.html', context)


def hot(request):
    context = {
        'title': 'Hot',
        'questions': Questions.objects.all().order_by('-amount_of_likes')
    }
    return render(request, 'main/index.html', context)


def question(request, question_id, page=1):
    main_question = Questions.objects.get(id=question_id)
    answer_context = Answers.objects.filter(question=question_id)
    context = {
        'question': main_question,
        'answers': paginate(answer_context, page, 3),
    }
    return render(request, 'main/question.html', context)


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
            return redirect('index')
        else:
            error = 'Wrong form!'

    form = QuestionForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/ask.html', context)




