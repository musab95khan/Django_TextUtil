from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyzed(request):
    Djtext = request.POST.get('text','default')
    RemovePunk = request.POST.get('removepunctuation','off')
    fullcaps = request.POST.get('fullcaps')
    spaceremove = request.POST.get('spaceremove')
    charcount = request.POST.get('charcount')

    if RemovePunk == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=""
        for char in Djtext:
            if char not in punctuations:
                analyze = analyze+char
        param = {'purpose':'removing punctuations','analyzed_text':analyze}
        Djtext=analyze

    if fullcaps =='on':
        analyze=''
        for char in Djtext:
            analyze=analyze+char.upper()
        param = {'purpose': 'Capitalizing', 'analyzed_text': analyze}
        Djtext=analyze

    if spaceremove =='on':
        analyze=''
        for char in Djtext:
            analyze = analyze+char.strip()
        param = {'purpose': 'removing extra space', 'analyzed_text': analyze}
        Djtext=analyze

    if charcount =='on':
        analyze=""
        for char in Djtext:
            analyze = analyze+char
            analyze_n = len(analyze)
        param = {'purpose': 'removing extra space', 'analyzed_text': analyze_n}
        Djtext=analyze_n

    if (RemovePunk != 'on' and fullcaps!='on' and spaceremove!='on' and charcount!='on'):
        return HttpResponse('Error')
    return render(request, 'analyzed.html', param)