from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie



def gift(request):
    # return HttpResponse("Hello world ! ")

    return render(request, 'HeartForSongJane/index.html', {})


def change_pic(request):
    return HttpResponse("Hello world ! ")