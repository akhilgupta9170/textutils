# I have created file -Akhil
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':

        punctuations = '''!@#$%^&*(){};"'.,:?~<>/'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed }

    #  analyze teh text
        djtext = analyzed

    if capitalize == "on":
        analyzed = ""
        for char in djtext:

            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'removed space', 'analyzed_text': analyzed}

    if removepunc != "on" and newlineremover != "on" and spaceremover != "on" and capitalize != "on":
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
