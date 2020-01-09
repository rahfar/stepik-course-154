from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignUpForm
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


@require_GET
def new(request):
    questions = paginate(request, Question.objects.new())
    return render(request, 'new.html', {
        'questions': questions
    })


@require_GET
def popular(request):
    questions = paginate(request, Question.objects.popular())
    return render(request, 'popular.html', {
        'questions': questions
    })


def question(request, qnum):
    question = get_object_or_404(Question, id=qnum)
    answers = Answer.objects.filter(question=qnum).all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_url())
        else:
            return render(request, 'question.html', {
            'question': question,
            'answers': answers,
            'form': form
        })
    else:
        form = AnswerForm()
        return render(request, 'question.html', {
            'question': question,
            'answers': answers,
            'form': form
        })
    


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            url = reverse('home')
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(url)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {
        'form': form
    })

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            url = reverse('home')
            return HttpResponseRedirect(url)
        else:
            form = AuthenticationForm(request.POST) 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {
        'form': form
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')
