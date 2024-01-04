from django import forms
from .models import Word, ThemeBlock


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['eng_word', 'rus_word']


class ThemeBlockForm(forms.ModelForm):
    class Meta:
        model = ThemeBlock
        fields = ['title', 'description', 'image']
