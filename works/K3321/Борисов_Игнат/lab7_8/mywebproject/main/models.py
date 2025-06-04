from django.db import models

# Create your models here.

class Feedback(models.Model):
    title = models.CharField('Заголовок', max_length=50, default="Title")
    full_text = models.TextField('Обратная связь')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'