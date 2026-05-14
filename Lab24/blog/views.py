from django.shortcuts import render
from .models import User, Media


def home(request):
    user = User(
        first_name='Аліна',
        last_name='Мороз',
        description='Це домашня сторінка користувача для курсової роботи.',
    )
    return render(request, 'blog/home.html', {'user': user})


def media_view(request):
    movie = Media(
        title='Дюна: Частина друга',
        description='Фантастичний фільм про пустельну планету Арракіс.',
        rating=9,
        studio_name='Warner Bros. Pictures'
    )
    return render(request, 'blog/media.html', {'media': movie})