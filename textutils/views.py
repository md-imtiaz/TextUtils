# Created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def AnalyzeText(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    WordCounter = request.POST.get('WordCounter', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+|='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': "Removed punctuations", 'analyzed_text': analyzed}
        djtext = analyzed

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
             analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed


    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        djtext = analyzed

    elif (WordCounter == 'on'):
        count = 0
        for char in djtext:
            if char == ' ':
                count += 1

        return HttpResponse("Your number of word is: " + str(count))

    else:
        return HttpResponse("please select any operation and try again")

    return render(request, 'TextAnalyzer.html', params)