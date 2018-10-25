from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'survey_form_app/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['favLang'] = request.POST['favLang']
    request.session['comment'] = request.POST['comment']
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] +=1
    return redirect('/result')

def result(request):
    return render(request, 'survey_form_app/result.html')

def reset(request):
    if 'count'in request.session:
        request.session['count'] = 0
    return redirect('/')