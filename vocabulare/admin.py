from django.contrib import admin
from .models import Word, ThemeBlock


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('rus_word', 'eng_word')
    search_fields = ('rus_word', 'eng_word')
    list_filter = ('rus_word', 'eng_word')
    list_per_page = 25


@admin.register(ThemeBlock)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    list_per_page = 25
