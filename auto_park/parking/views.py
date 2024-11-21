from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator


def index(request):

    return render(request, "home.html")