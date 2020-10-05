from django.shortcuts import render
from issue.models import Issue, Community
from django.views import generic
from el_pagination.decorators import page_template


# Create your views here.
class IndexView(generic.ListView):
    model = Issue
    template_name = 'main.html'


@page_template('parts/issue_list.html')  # just add this decorator
def issue_list(request, template='main.html', extra_context=None):
    issue_list = Issue.objects.all()
    if request.GET.get('keyword'):
        issue_list = issue_list.filter(title__contains=request.GET.get('keyword'))
    context = {
        'issue_list': issue_list.order_by('-date'),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
