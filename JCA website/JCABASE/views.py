from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection


# Create your views here.

def home(request):
    teachers = Teachers.objects.all()
    parent_reviews = Parents_review.objects.all()
    news_latest = News.objects.all()[0:4]
    blog_latest = Blog.objects.all()[0:4]

    context = {'teachers': teachers, 'parent_reviews': parent_reviews, 'news_latest': news_latest,
               'blog_latest': blog_latest}
    return render(request, 'JCABASE/index.html', context)


def about(request):
    return render(request, 'JCABASE/about.html')


def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'JCABASE/news.html', context)


def news_details(request, pk):
    news_detail = News.objects.get(id=pk)
    context = {'news_detail': news_detail}
    return render(request, 'JCABASE/news_detail.html', context)


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'JCABASE/blogs.html', context)


def blogDetails(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, 'JCABASE/blog_detail.html', context)


def newsForm(request):
    form = NewsForm()

    if request.method == 'POST':
        News.objects.create(
            news_pic=request.POST.get('news_pic'),
            news_title=request.POST.get('news_title'),
            news_content=request.POST.get('news_content')
        )
        return redirect('news')

    context = {'form': form}
    return render(request, 'JCABASE/news_form.html', context)


def blogForm(request):
    form = BlogForm()

    if request.method == 'POST':
        Blog.objects.create(
            blog_pic=request.POST.get('blog_pic'),
            writer=request.POST.get('writer'),
            blog_title=request.POST.get('blog_title'),
            paragraph=request.POST.get('paragraph')
        )
        return redirect('blogs')

    context = {'form': form}
    return render(request, 'JCABASE/blog_form.html', context)


def contact(request):
    form = ContactForm()

    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'richlueking302@gmail.com'),
                ['example@gmail.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact?submitted=True')
        else:
            if 'submitted' in request.GET:
                submitted = True

    context = {'form':form, 'submitted': submitted}
    return render(request, 'JCABASE/contact.html', context)


