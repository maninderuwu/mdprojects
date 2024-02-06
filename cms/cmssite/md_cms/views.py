from django.shortcuts import render ,get_object_or_404, redirect 
from .models import Article
from .forms import ArticleForm ,SearchForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout

# Create your views here.
def home(request):
    return render(request, 'index.html')


def article_list(request):
    articles = Article.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        articles=articles.filter(title__icontains=search_query)
        return render(request, 'search_result.html', {'articles': articles, 'search_query': search_query})
        
    return render(request , 'article_list.html',{'articles':articles, 'search_form':search_form})

def article_details(request , pk):
    article = get_object_or_404(Article , pk=pk)
    return render (request , 'article_details.html',{'article':article})

@login_required
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
         form = ArticleForm()
    return render(request, "add_article.html", {'form':form})

def edit_article(request, pk):
    article = get_object_or_404(Article,pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'cms_app/edit_article.html', {'form': form, 'article': article})

def delete_article(request, pk):
    article = get_object_or_404(Article , pk=pk)
    article.delete()
    return redirect('article_list')

def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article_list')
    
    else:
        form=UserCreationForm()

    return render(request, 'signup.html', {'form': form})
    
def logout_user(request):
    logout(request)
    return redirect('article_list')

