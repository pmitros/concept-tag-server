import sys
import json

from collections import OrderedDict

from django.shortcuts import render

from django.http import HttpResponse

from wiki.models.urlpath import URLPath
from wiki.models.article import Article

def JSONResponse(r):
    response = HttpResponse(json.dumps(r))
    response['Access-Control-Allow-Origin']  = '*'
    response['Access-Control-Allow-Methods'] = "GET"
    return response

def sample(request):
    return HttpResponse("Hello!")

def get_concept_list(request):
    try:
        query = request.GET['q']
        print query
        results_slug = [u.slug for u in URLPath.objects.filter(slug__contains = query) if u.slug]
        results_article = [u.slug for u in URLPath.objects.all() if query in URLPath.objects.get(slug=u.slug).article.render()]
        results_title = [u.slug for u in URLPath.objects.all() if query in URLPath.objects.get(slug=u.slug).article.current_revision.title]
        results = list(OrderedDict.fromkeys(results_slug + results_title + results_article))
        return JSONResponse(results)
    except: 
        print sys.exc_info()
        raise

def get_concept(request, name):
    article = URLPath.objects.get(slug=name).article.render()
    title = URLPath.objects.get(slug=name).article.current_revision.title
    return JSONResponse({'article':article,
                         'title':title, 
                         'slug':name})

