from django.shortcuts import render
from .forms import section

# Create your views here.

listOfPosts = []

def posts(request):
    Section = section()
    return render(request, 'posts.html', {'form': Section})

def allPosts(request):
    heading = request.GET.get('Heading')
    url = request.GET.get('URL')
    content = request.GET.get('Content')
    publication = request.GET.get('Publication')
    category = request.GET.get('Category')
    post = [heading, url, content, publication, category]
    listOfPosts.append(post)
    return render(request, 'allPosts.html', {'form': [listOfPosts[i] for i in range(len(listOfPosts))]})