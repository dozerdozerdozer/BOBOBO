
from django.contrib import admin
from .models import Questions, Answers, Tags, Users


admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Users)
admin.site.register(Tags)

