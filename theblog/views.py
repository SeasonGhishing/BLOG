from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost

class PostList(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostCreate(CreateView):
    model = BlogPost
    template_name = 'blog/post_create.html'
    fields = ['title', 'uploaded_by', 'created_date', 'description', 'image']
    success_url = reverse_lazy('blog:post_list')

class PostDetail(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostUpdate(UpdateView):
    model = BlogPost
    template_name = 'blog/post_update.html'
    fields = ['title', 'uploaded_by', 'created_date', 'description', 'image']
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')

class PostDelete(DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:post_list')
