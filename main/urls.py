
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('tag/<tag_id>/', views.tag, name='tag'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]
