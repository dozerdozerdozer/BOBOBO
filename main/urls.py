
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('tag/<tag_id>/', views.tag, name='tag'),
    path('question/<int:question_id>/', views.add_answer, name='question'),
    path('ask/', views.add_question, name='ask'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.log_out, name='logout'),
    path('profile/change_password/', views.change_password, name='change_password'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
