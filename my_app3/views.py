from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Author, Post


def hello(request):
    return HttpResponse('Hello!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello from class!')


def year_post(request, year):
    text = 'some text'
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, request, year, month):
        text = 'some text'
        return HttpResponse(f'Posts from {year}, {month}<br>{text}')


def post_detail(request, year, month, slug):
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'Название статьи',
        'content': 'Полный текст статьи'
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {'name': 'Hern'}
    return render(request, 'my_app3/my_template.html', context)


class TemplIf(TemplateView):
    template_name = "my_app3/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 1
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'my_app3/templ_for.html', context)


def index(request):
    return render(request, 'my_app3/index.html')


def about(request):
    return render(request, 'my_app3/about.html')


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'my_app3/posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'my_app3/post_full.html', {'post': post})
