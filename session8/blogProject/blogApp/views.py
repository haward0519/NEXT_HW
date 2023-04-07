from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

def Home(request):
    return render(request, 'home.html')

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

def list(request):
    Exercises = Article.objects.filter(category='Exercise')
    Exercises_len = Exercises.count()

    Foods = Article.objects.filter(category='Food')
    Foods_len = len(Foods)

    Startups = Article.objects.filter(category='Startup')
    Startups_len = len(Startups)

    return render(request, 'home.html', {'Exercises_len': Exercises_len, 'Foods_len': Foods_len, 'Startups_len': Startups_len})

def detail(request, article_id):
   if request.method == 'GET':
        list_article = Article.objects.get(pk=article_id)
        created_dt = article_detail.dt
        return render(request, 'detail.html', {'article': list_article, 'created_dt':created_dt})
   
def category(request, category_kind):
    category_kind_templates = category_kind
    categorized_articles = Article.objects.filter(category=category_kind)
    return render(request, 'list.html', {'categorized_articles': categorized_articles, 'category_kind_templates':category_kind_templates,})
   