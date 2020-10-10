from django.shortcuts import render
from issue.models import Issue, Community
from el_pagination.decorators import page_template


@page_template('parts/issue_list.html')  # just add this decorator
def issue_list(request, template='main.html', extra_context=None):
    issue_list = Issue.objects.all()
    community_list = Community.objects.all()
    # if request.path == '/filter/':  # 왼쪽 필터 적용 할 경우
    if request.GET.get('pp'):
        site_list = [site_key for site_key, site_value in request.GET.dict().items() if site_value == 'true']
        issue_list = issue_list.filter(site__site__in=site_list)
    # elif request.path == '/search/':
    #     issue_list = issue_list.filter(title__in=request.GET.get('keyword'))
    context = {
        'issue_list': issue_list.order_by('-date'),
        'community_list': community_list,
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
