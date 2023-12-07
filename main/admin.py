
from django.contrib import admin
from .models import *


admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(User)
admin.site.register(Tags)
admin.site.register(QuestionLikes)
admin.site.register(AnswerLikes)

