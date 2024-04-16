from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
from .forms import PostForm

# Create your views here.

class PostView(ListView):
    model = Post
    template_name = 'bulletin_board/post.html'
    context_object_name = 'posts'


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



    