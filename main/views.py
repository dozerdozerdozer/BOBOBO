from django.shortcuts import HttpResponseRedirect, render, redirect
from .services import *
from .forms import *
from django.contrib import auth, messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def base_context(request):
    best_users = User.objects.best_users(5)
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


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'main/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, "Invalid username or password")
        else:
            print(f"Form is invalid: {form.errors}")
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'main/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(request, "Congratulations! You have successfully registered.")
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'main/registration.html', context)


def log_out(request):
    logout(request)
    return index(request)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'main/change_password.html', {'form': form})


@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            tags_input = form.cleaned_data['tags']

            if isinstance(tags_input, str):
                tag_list = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
            else:
                tag_list = tags_input

            que = form.save(commit=False)
            que.author = request.user
            que.save()

            tags_objects = [Tags.objects.get_or_create(tag_name=tag)[0] for tag in tag_list]
            que.tags.set(tags_objects)

            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'main/ask.html', {'form': form})


@login_required
def add_answer(request, question_id):
    print(request.POST)
    que = get_object_or_404(Questions, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = que
            answer.save()

            answers = Answers.objects.filter(question=que).order_by('date_written')
            paginator = Paginator(answers, 3)
            page_number = paginator.num_pages

            return redirect(answer.get_absolute_url(page_number))
    else:
        form = AnswerForm()

    context = {
        'form': form,
        'question': que,
        'answers': paginate(request, Answers.objects.filter(question=question_id), 3),
    }
    return render(request, 'main/question.html', context)
