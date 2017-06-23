from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
from article.forms import CommentForm
from article.models import Article, Comments


def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is sparta!!! %s </body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    html = get_template('myview.html').render({'name': view})
    return HttpResponse(html)


def template_three(request):
    view = 'template three'
    return render(request, 'myview.html', {'name': view})


def articles(request, page_number=1):
    all_articles = Article.objects.all()
    pages = Paginator(all_articles, 2)
    try:
        current_page = pages.page(page_number)
    except EmptyPage:
        raise Http404
    return render(request, 'articles.html', {'articles': current_page, 'username': auth.get_user(request).username})


def article(request, article_id=1, page_number=1):
    comment_form = CommentForm
    all_comments = Comments.objects.filter(comments_article_id=article_id)
    pages = Paginator(all_comments, 2)
    try:
        current_page = pages.page(page_number)
    except EmptyPage:
        raise Http404
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = current_page
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id, page_number):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_like += 1
            article.save()
            response = redirect('/page/' + page_number)
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/page/' + page_number)

def addcomment(request, article_id, page_number):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/article/get/%s/' % article_id + page_number)