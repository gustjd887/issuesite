from urllib.parse import unquote
from django.db.models import Q
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
    community_list = Community.objects.exclude(site='total')
    site_list = []
    if request.get_full_path()[1:7] == 'filter': # 왼쪽 필터 적용 할 경우
        for site_key, site_value in request.GET.dict().items():
            if site_value == 'true':
                site_list.append(site_key)
        issue_list = issue_list.filter(site__site__in=site_list)
    context = {
        'issue_list': issue_list.order_by('-date'),
        'community_list': community_list,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
