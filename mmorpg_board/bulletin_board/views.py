from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from users.models import User
from .models import Post
from .forms import PostForm
import bleach
# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'bulletin_board/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().order_by('-date')
    


class UserPostListView(ListView):
    model = Post
    template_name = 'bulletin_board/user_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Получаем имя пользователя из URL
        username = self.kwargs.get('username')
        # Фильтруем посты только для пользователя с указанным именем
        return Post.objects.filter(author__username=username).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем имя пользователя из URL-адреса
        username = self.kwargs['username']
        context['username'] = username
        user = User.objects.get(username=username)
        user_post_count = user.post_set.count()
        context['user_post_count'] = user_post_count
        return context
    
    
class PostDetail(DetailView):
    model = Post
    template_name = 'bulletin_board/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = context['object']
        return context
    

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'bulletin_board/post_create.html'
    raise_exception = True

    def form_valid(self, form):
        # Присваиваем текущего пользователя в качестве автора поста
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def get_posts_by_user(request, username):
    # Находим пользователя по его имени
    user = User.objects.get(username=username)

    # Получаем посты, созданные выбранным пользователем
    posts = Post.objects.filter(author=user)

    # Преобразуем данные в формат JSON и отправляем обратно клиенту
    posts_data = [{'title': post.title, 'text': post.text} for post in posts]
    return JsonResponse(posts_data, safe=False)    



    