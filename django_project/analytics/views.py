from django.shortcuts import render
from .models import PageView

# Create your views here.

# views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from analytics!")


def page_view_list(request):
    page_views = PageView.objects.all()
    return render(request, 'analytics/page_view_list.html', {'page_views': page_views})