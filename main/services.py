from .models import *
from .views import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate(request, objects, per_page=3):
    # page - номер страницы, которую нужно отобразить (по умолчанию 1)
    # per_page - кол-во элементов на странице *по умолчанию 10)

    page_num = request.GET.get('page')
    paginator = Paginator(objects, per_page)
    try:
        que = paginator.page(page_num)
    except PageNotAnInteger:
        que = paginator.page(1)
    except EmptyPage:
        que = paginator.page(paginator.num_pages)
    return que


def index_context(request):
    context = {
        'title': 'Home Page',
        'questions': paginate(request, Questions.objects.all().order_by('-id'), 20),
    }
    return context


def tag_context(request, tag_id):
    try:
        tag_id = int(tag_id)
        teg = get_object_or_404(Tags, id=tag_id)
    except ValueError:
        tag_id = 1
        try:
            teg = Tags.objects.get(id=tag_id)
        except ObjectDoesNotExist:
            teg = Tags.objects.last()
    except Tags.DoesNotExist:
        teg = Tags.objects.last()
    context = {
        'title': f'{teg}',
        'questions': paginate(request, Questions.objects.filter(tags=teg).order_by('-id'))
    }
    return context


def hot_context(request):
    context = {
        'title': 'Hot',
        'questions': paginate(request, Questions.objects.all().order_by('-amount_of_likes'))
    }
    return context


def question_context(request, question_id):
    context = {
        'question': Questions.objects.get(id=question_id),
        'answers': paginate(request, Answers.objects.filter(question=question_id), 3),
    }
    return context
