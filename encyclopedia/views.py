from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import encyclopedia


def index(request):
    query = request.GET.get('q')    # return QueryDict
    entries = util.list_entries()
    filtered = filter(lambda e: query in e, entries) 

    if query in entries:
        # print(type(entries), entries)
        # print(type(filtered), filtered)
        return HttpResponseRedirect(reverse('wiki', args=[query]))
        # return HttpResponse(query)
    elif any(str(query) in e for e in entries):
        return render(request, "encyclopedia/result.html", {
            "entries": filtered
        })
        

    # if query in entries:
    #     return HttpResponseRedirect(reverse('wiki', args=[query]))        
    # elif any(query in s for s in entries):
    #     return HttpResponse()
    #     # entries = [s for s in entries if query in s] 

    return render(request, "encyclopedia/index.html", {
        "entries": entries
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
    