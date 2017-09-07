from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Question, Choice
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # render模板渲染
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    # request常见属性都可以通过request对象获取
    #       META HTTP_REFERER, HTTP_USER_AGENT, REMOTE_ADDR
    #       schema method COOKIES FILES
    #       path, get_host, get_full_path, is_secure
    # 可以快速的去数据库查询主键是id的数据，如果有报错就自己处理了
    # get_object_or_404直接查找数据,不用多写代码(tre)
    # get_list_or_404 如果是空的就会返回404
    question = get_object_or_404(Question, pk=question_id)
    # request.FILES
    # request.GET
    # 如果表单中提交了一个文件(GET),要通过FILES获取,
    if request.method == 'POST':
        # 可以通过request的Post拿到里面的内容
        choice_id = request.POST.get('choice', 0)
        try:
            # 通过p对象反查出选项
            selected_choice = question.choice_set.get(pk=choice_id)
        except Choice.DoesNotExist:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # HttpResponseRedirect 重定向
            # redirect 快速的重定向到某个url
            return HttpResponseRedirect(reverse('results', args=(question.id,)))