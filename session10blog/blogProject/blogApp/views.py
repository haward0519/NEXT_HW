from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

# Create your views here.

def Home(request):
    Exercises = Article.objects.filter(category='Exercise')
    Exercises_count = Exercises.count()

    Foods = Article.objects.filter(category='Food')
    Foods_count = Foods.count()

    Startups = Article.objects.filter(category='Startup')
    Startups_count = Startups.count()

    return render(request, 'home.html', {
        'Exercises_count': Exercises_count, 'Foods_count': Foods_count, 'Startups_count': Startups_count})

def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(

            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        
        return redirect('Home')
    return render(request, 'new.html')


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    
    return render(request, 'detail.html', {'article': article})

def comment(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('comment', article.pk)
    return render(request, 'comment.html', {'article': article})

def delete_comment(request, article_id, comment_id):
   comment = Comment.objects.get(pk=comment_id)
   comment.delete()
   return redirect('comment', article_id)


def recomment(request, article_id, comment_id):
    article = Article.objects.get(pk=article_id)
    comment = Comment.objects.get(pk=comment_id)

    if request.method == "POST":
        content = request.POST['content']
        Recomment.objects.create(
            comment = comment,
            content = content
        )
        return redirect('recomment', article.pk, comment.pk)
    return render(request, 'recomment.html', {'article': article, 'comment': comment})

def recomment_delete(request, article_id, comment_id, recomment_id):
    recomment = Recomment.objects.get(pk=recomment_id)
    recomment.delete()
    return redirect('recomment', article_id, comment_id)

def category(request, category_kind):
    category_kind_templates = category_kind
    categorized_articles = Article.objects.filter(category=category_kind)
    return render(request, 'list.html', {'categorized_articles': categorized_articles, 'category_kind_templates':category_kind_templates,})


