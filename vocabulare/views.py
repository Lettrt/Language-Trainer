from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db import models
from .models import ThemeBlock, Word
from .forms import WordForm, ThemeBlockForm
import random
import json


def study_words(request, pk, mode):
    words = Word.objects.filter(theme=pk)
    if not words.exists():
        return render(request, 'vocabulare/no_words.html')

    words_list = list(words.values('eng_word', 'rus_word'))
    random.shuffle(words_list)

    words_json = json.dumps(words_list)

    return render(request, 'vocabulare/study_words.html',
                  {
                      'words_json': words_json,
                      'total_words_count': words.count(),
                      'mode': mode
                   }
                  )


class HomeView(ListView):
    model = ThemeBlock
    template_name = 'vocabulare/home.html'
    context_object_name = 'theme_blocks'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            words_count=models.Count('words')
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ThemeBlockDetailView(DetailView):
    model = ThemeBlock
    template_name = 'vocabulare/theme_detail.html'
    context_object_name = 'theme_block'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = self.object.words.all()
        return context


class AddWordView(CreateView):
    model = Word
    form_class = WordForm
    template_name = 'vocabulare/add_word_form.html'

    def form_valid(self, form):
        form.instance.theme = ThemeBlock.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('theme_detail', kwargs={'pk': self.kwargs['pk']})


class ThemeBlockCreateView(CreateView):
    model = ThemeBlock
    form_class = ThemeBlockForm
    template_name = 'vocabulare/add_theme.html'

    def get_success_url(self):
        return reverse_lazy('theme_detail', kwargs={'pk': self.object.pk})
