from django.shortcuts import render
from issue.models import Issue, Community
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    model = Issue
    template_name = 'main.html'