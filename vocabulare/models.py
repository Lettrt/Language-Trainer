from django.db import models


def theme_directory_path(instance, filename):
    return f'themes/{instance.title}/{filename}'


class ThemeBlock(models.Model):
    """
    Модель тематического блока
    - title (str):
        название блока
    - description (str):
        описание блока
    """
    title = models.CharField(
        max_length=200,
        verbose_name='Название блока'
    )
    description = models.TextField(
        verbose_name='Описание блока'
    )
    image = models.ImageField(
        upload_to=f'themes/{title}'
    )

    def __str__(self):
        return f'{self.title}: {self.description[:25]}...'

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'


class Word(models.Model):
    """
    Модель региона.
    - rus_word (str):
        русское слово.
    - eng_word (str):
        английское слово
    """

    rus_word = models.CharField(
        max_length=150, db_index=True,
        verbose_name='russian words'
    )
    eng_word = models.CharField(
        max_length=150, db_index=True,
        verbose_name='english words'
    )
    theme = models.ForeignKey(
        ThemeBlock, related_name='words',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.rus_word} - {self.eng_word}'

    class Meta:
        verbose_name = 'Word'
        verbose_name_plural = 'Words'
