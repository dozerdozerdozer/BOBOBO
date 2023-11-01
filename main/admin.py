
from django.contrib import admin
from .models import Question, Answers, Tags, Users


admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Users)
admin.site.register(Tags)

