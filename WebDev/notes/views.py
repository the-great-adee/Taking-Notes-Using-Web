from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Notes
from django.shortcuts import render

def index(request):
    mynotes = Notes.objects.all().values()
    template = loader.get_template('demo.html')
    context = {
        'mynotes': mynotes,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['title']
    y = request.POST['description']
    notes = Notes(title=x, description=y)
    notes.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    notes = Notes.objects.get(id = id)
    notes.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mynotes = Notes.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'mynotes':mynotes,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    title = request.POST['title']
    description = request.POST['description']
    notes = Notes.objects.get(id=id)
    notes.title = title
    notes.description = description
    notes.save()
    return HttpResponseRedirect(reverse('index'))
