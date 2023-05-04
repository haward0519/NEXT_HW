from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Article, Comment, User


# Create your views here.

def Home(request):
    Exercises = Article.objects.filter(category='Exercise')

    Foods = Article.objects.filter(category='Food')


    Startups = Article.objects.filter(category='Startup')
    

    return render(request, 'blog/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        exist_user = User.objects.filter(username=username)
        
        if exist_user:
            user_error = "해당 유저가 이미 존재합니다."
            return render(request, 'blog/signup.html', {'user_error': user_error})

        new_user = User.objects.create_user(
            username = username,
            password = password
        )

        auth.login(request, new_user)
        return redirect('blog:Home')
    return render(request, 'blog/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('blog:Home')
    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'blog/home.html')

def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(

            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        
        return redirect('blog:Home')
    return render(request, 'blog/new.html')


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    
    return render(request, 'blog/detail.html', {'article': article})

def comment(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('blog:comment', article.pk)
    return render(request, 'blog/comment.html', {'article': article})

def delete_comment(request, article_id, comment_id):
   comment = Comment.objects.get(pk=comment_id)
   comment.delete()
   return redirect('blog:comment', article_id)


def category(request, category_kind):
    category_kind_templates = category_kind
    categorized_articles = Article.objects.filter(category=category_kind)
    return render(request, 'blog/list.html', {'categorized_articles': categorized_articles, 'category_kind_templates':category_kind_templates,})

def all(request, user_pk):
    posts = Article.objects.all()
    return render(request, 'blog/all.html', {'posts': posts})

