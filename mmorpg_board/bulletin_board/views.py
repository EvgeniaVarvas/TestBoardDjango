from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

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


    