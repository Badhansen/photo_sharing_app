from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from posts.models import Post

class PostList(ListView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['image', 'description', 'author']
    success_url = '/'
