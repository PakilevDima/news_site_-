from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *


# Create your views here.

def home_view(request, category_id: int = None):

    if category_id == None:
        categories = Category.objects.all()
        news = News.objects.filter(status='published')
        paginator = Paginator(news, 3)  # По 3 статьи на каждой странице
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, "home.html", {"page": page, "news": posts, "categories": categories})
    else:
        categories = Category.objects.all()
        news = News.objects.filter(category=category_id)
        paginator = Paginator(news, 2)  # Show 2 contacts per page.
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, "other.html", {"page": page, "other": posts, "categories": categories})



@login_required(login_url='/accounts/login/')
def detail_view(request, id):
    if request.user.is_authenticated == False:
        return render(request, "sign_up.html")
    else:
        post = get_object_or_404(News, id=id)

        return render(request, "detail.html", {"post": post, "categories": post.category.all()})


def about(request):
    return render(request, 'about.html', {'about': []})










class MoviesCreateView(CreateView):
    model = News
    template_name = 'movie_new.html'
    fields = '__all__'

class MoviesUpdateView(UpdateView):
    model = News
    fields = ['title', 'content_text', 'category', "image", "date"]
    template_name = 'movie_edit.html'

class MoviesDeleteView(DeleteView):
    model = News
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('home')



class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_new.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = '__all__'
    success_url = reverse_lazy('home')