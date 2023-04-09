from django.shortcuts import render, redirect
from .models import Post 
from datetime import datetime
# Create your views here.


def home(request):
    posts = Post.objects.order_by('date')
    post_ddays = [calculate_dday(post.date) for post in posts]

    context = {
        'posts': zip(posts, post_ddays)
        # post 객체와 D-day 값을 튜플 형태로 묶어서 전달
    }

    return render(request, 'home.html', context)

# def home(request):
    #posts = Post.objects.order_by('date')

   # return render(request, 'home.html', {'posts': posts})

def homedday(request):
    posts = posts = Post.objects.all
    ddays = calculate_dday(posts.date)
    return render(request, 'detail.html', {'post': post, 'dday': dday})

def new(request):
    if request.method == 'POST':
        post = Post.objects.create(
            title = request.POST['title'],
            date = request.POST['date'],
            content = request.POST['content']        
        )
        return redirect('detail', post.pk)

    return render(request, 'new.html')

def calculate_dday(post_date):
    today = datetime.today().date()
    dday = (post_date - today).days

    return dday

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    dday = calculate_dday(post.date)
    return render(request, 'detail.html', {'post': post, 'dday': dday})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            date = request.POST['date'],
            content = request.POST['content']        
        )

        return redirect('detail', post_pk)

    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

