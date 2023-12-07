from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import *
from django.contrib import auth


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
        'questions': paginate(request, Questions.objects.all_best_questions(), 20),
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
        'questions': paginate(request, Questions.objects.this_tag_questions(tag_id).order_by('-id'))
    }
    return context


def hot_context(request):
    context = {
        'title': 'Hot',
        'questions': paginate(request, Questions.objects.hot_questions())
    }
    return context



