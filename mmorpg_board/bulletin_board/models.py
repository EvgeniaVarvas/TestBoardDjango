from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings


# Create your models here.
class Post(models.Model):
    TYPE = [
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('dd', 'ДД'),
        ('traders', 'Торговцы'),
        ('guildmasters', 'Гильдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('letherworkers', 'Кожевники'),
        ('alchemists', 'Зельевары'),
        ('spellcasters', 'Мастера заклинаний')
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=20, choices=TYPE)
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        # Возвращаем URL-адрес для просмотра этого объекта Post
        return reverse('post_detail', kwargs={'pk': self.pk})


class Response(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author.username} - {self.text}'
