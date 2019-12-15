from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
# Create your views here.
from django.http import HttpResponse
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


@require_GET
def question(request, qnum):
    question = get_object_or_404(Question, id=qnum)
    return render(request, 'question.html', {
        'question': question
    })


@require_GET
def main(request):
    return render(request, 'main.html')


@require_GET
def popular(request):
    return HttpResponse('OK')


def test(request, *args, **kwargs):
    return HttpResponse('OK')
