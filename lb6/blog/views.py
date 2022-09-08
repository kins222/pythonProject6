from django.views.generic import ListView
from .models import Post

class BlogListView(listView):
    model = Post
    template_name='home.html'

# Create your views here.
