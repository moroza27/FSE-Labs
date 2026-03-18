from django.shortcuts import render

def home(request):
    context = {
        'title': 'Головна сторінка',
        'message': 'Привіт, Django!'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')