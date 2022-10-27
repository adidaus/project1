from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


def index(request):
    query = request.GET.get('q')

    if query:
        return HttpResponseRedirect(reverse('wiki', args=[query]))        

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    query = request.GET.get('q')

    if query:
        return HttpResponseRedirect(reverse('wiki', args=[query]))

    entry = util.get_entry(title)

    if (entry):
        return render(request, 'encyclopedia/wiki.html', {
            'entry': entry,
            'title': title
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            'title': title,
            'msg': f"Error: '{title}' not found."
        })

# def search(request):
#     result = request.GET.get('q')
#     return HttpResponse(result)
    