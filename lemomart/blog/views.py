from django.shortcuts import render

from . models import blogpost

# Create your views here.
def index(request):
   return render(request, 'blog/index.html')

def blogPost(request, bid):
   post = blogpost.objects.filter(post_id = bid)[0]
   return render(request, 'blog/blogpost.html', {'post': post})