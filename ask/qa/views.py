from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.http import HttpResponse, Http404
from qa.models import Question, Answer


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



@require_GET
def question(request, qnum):
    question = get_object_or_404(Question, id=qnum)
    answers = Answer.objects.filter(question=qnum).all()
    return render(request, 'question.html', {
        'question': question,
        'answers': answers
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')
