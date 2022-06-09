import string
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #getting the text
    dj_text=request.POST.get('text','default')
    #checkbox values
    removepunc =request.POST.get('removepunc','off')
    fullcaps =request.POST.get('fullcaps','off')
    capitaliz =request.GET.get('capitaliz','off')
    newlineremover =request.POST.get('newlineremover','off')
    extraspace =request.POST.get('extraspace','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation','analyzed_text':analyzed}
        dj_text=analyzed
        #return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed =""
        for char in dj_text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case','analyzed_text':analyzed}   
        dj_text=analyzed
        #return render(request, 'analyze.html', params)

    if capitaliz == "on":
        analyzed=" "
        analyzed = string.capwords(dj_text)
        #for char in dj_text:
           # analyzed = analyzed + char.capwords()
    ##        
        params = {'purpose': 'First letter capitalize ','analyzed_text':analyzed}   
    ##    return render(request, 'analyze.html', params)
        dj_text=analyzed

    if newlineremover == "on":
        analyzed =""
        for char in dj_text:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line removed','analyzed_text':analyzed}   
        dj_text=analyzed
        #return render(request, 'analyze.html', params) 
    if extraspace == "on":
        analyzed =""
        for index, char in enumerate(dj_text):

            if  dj_text[index] ==" " and dj_text[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra space removed','analyzed_text':analyzed}   
       
        #return render(request, 'analyze.html', params)   
    #return render(request, 'analyze.html', params)  
    if (removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspace!="on"):
        #return HttpResponse("Text not found")
        return render(request, 'error.html',)
    
    else:
        return render(request, 'analyze.html', params) 
    
    
