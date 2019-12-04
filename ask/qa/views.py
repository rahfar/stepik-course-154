from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
# Create your views here.
from django.http import HttpResponse
from qa.models import Question, Answer

@require_GET
def question(request):
    question = get_object_or_404(Question, id=request.qnum)
    return render(request, 'question.html', {
        'question': question
    })


@require_GET
def popular(request):
    pass


def test(request, *args, **kwargs):
    return HttpResponse('OK')
