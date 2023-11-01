from .models import Question, Answers
from django.forms import ModelForm, TextInput, Textarea


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["title", "text"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short description for your question'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your question here'
            }),
        }



