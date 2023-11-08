from .models import Questions, Answers
from django.forms import ModelForm, TextInput, Textarea


class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ["title", "text", "tags"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write a short description for your question'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your question here'
            }),
            "tags": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Write tags here'
            }),
        }


class AnswerForm(ModelForm):
    class Meta:
        model = Answers
        fields = ['answer_text']
        widgets = {
            "answer_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your question here'
            })
        }



