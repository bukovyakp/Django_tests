#coding:utf-8

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context                           # Зберігає перемінні, які будуть підтягуті у ХТМЛ сторінку
from django.shortcuts import render_to_response, redirect     # Рендер у відповідь відразу
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.core.context_processors import csrf
from django.contrib import auth

from forms import CommentForm

# Create your views here.

def basicone(request):
    view = "basic_one"
    html = "<html><body> This is %s view </html></body>" % view
    return HttpResponse(html)

def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))    # генерує фінальний ХТМЛ код
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three"
    return render_to_response('myview.html', {'name': view})    # третій спосіб відображення в'юх

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all(), 'username': auth.get_user(request).username})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

    #   Нижче попередня версія функції article
    #   return render_to_response('article.html', {'article': Article.objects.get(id=article_id),
    #                                              'comments': Comments.objects.filter(comments_article_id=article_id)})

def addlike(request, article_id):                               # Додаємо кількість лайків по натисканні на кнопку
    try:
        if article_id in request.COOKIES:                          # for cookie
            redirect('/')                                          # for cookie
        else:                                                      # for cookie
            article = Article.objects.get(id=article_id)
            article.article_like += 1
            article.save()
            response = redirect('/')                                # for cookie
            response.set_cookie(article_id, "test")                 # for cookie
            return response                                         # for cookie
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):           # метод POST + for session
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)                           # for session
            request.session['pause'] = True                          # for session
    return redirect('/articles/get/%s/' % article_id)

