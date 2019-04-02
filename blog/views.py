from django.shortcuts import render

posts = [
    {
       'author': 'CoreyMS',
       'title': 'Blog post 1',
       'content': 'First post',
       'date_posted': 'August 27, 2018' 
    },
        {
       'author': 'CoreyMS2',
       'title': 'Blog post 2',
       'content': 'First post 2',
       'date_posted': 'August 27, 2018 2' 
    },
        {
       'author': 'CoreyMS3',
       'title': 'Blog post 3',
       'content': 'First post 3',
       'date_posted': 'August 27, 2018 3' 
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': 'home page'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')