from django.http import HttpResponse
from django.shortcuts import render
from . import counter


def home(request):
    return render(request,'index.html',{'some_hidden':'I am from view page..'})

def result(request):
    article = request.GET['article']
    var_dict,words_count = counter.count(article)

    return render(request,'result.html',{'article' : article,'count':words_count,'dict_word':var_dict})


