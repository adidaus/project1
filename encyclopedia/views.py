from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, title):
    entry = util.get_entry(title)

    if (entry):
        return render(request, 'encyclopedia/wiki.html', {
            'entry': entry 
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            'title': title,
            'msg': f'Error: {title} not found.'
        })
