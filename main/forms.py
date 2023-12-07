from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import *
from django import forms
from django.forms import Textarea


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your Email'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your nickname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2',
        'placeholder': 'Enter your username'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2', 'readonly': True}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-2'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-2', 'readonly': True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'nickname', 'image')

    def save(self, **kwargs):
        user = super().save(**kwargs)

        user.image = self.cleaned_data.get('image')
        user.save()

        return user


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Repeat new password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Enter your title'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control py-2', 'placeholder': 'Enter your question'}))
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-2', 'placeholder': 'Enter your tags'}))

    class Meta:
        model = Questions
        fields = ('title', 'text', 'tags')

    def clean_tags(self):
        raw_tags = self.cleaned_data['tags']
        return [tag.strip() for tag in raw_tags.split(',') if tag.strip()]


class AnswerForm(forms.ModelForm):
    answer_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control py-2',
                'rows': 3,
                'placeholder': 'You can write your answer here!'
            }))

    class Meta:
        model = Answers
        fields = ('answer_text',)
