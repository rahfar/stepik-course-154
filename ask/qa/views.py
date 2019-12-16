from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
from django.http import HttpResponse, Http404
from qa.models import Question, Answer


# posts = [
#     {
#         'title': 'first',
#         'author': 'Fred',
#         'flg': 123
#     },
#     {
#         'title': 'second',
#         'author': 'Ann'
#     }
# ]
def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 5))
    except ValueError:
        limit = 5
    if limit > 100:
        limit = 5
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
def main(request):
    questions = paginate(request, Question.objects.new())
    return render(request, 'main.html', {
        'questions': questions
    })


@require_GET
def popular(request):
    return HttpResponse('OK')


@require_GET
def question(request, qnum):
    question = get_object_or_404(Question, id=qnum)
    return render(request, 'question.html', {
        'question': question
    })


def test(request, *args, **kwargs):
    return HttpResponse('OK')
