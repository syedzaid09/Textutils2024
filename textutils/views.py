# I have created this file- Zaid
from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
 #   #file = open("E:\data analytics\one.txt")
    #fdata = file.read()
  #  return HttpResponse("""<h1>Harry</h1>  <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list
  #  =PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django CodewithHarry</a>""")


#def about(request):
 #   return HttpResponse("About")

def index(request):
    return render(request,'index.html')

def ex1(request):
    s=['''<h1>For Entertainment</h1>
    <a href="https://www.facebook.com/">Facebook</a>''',
    '''<h1>For Interaction</h1><a href="https://www.flipkart.com/">Flipkart</a><br>''',
    '''<h1>For News</h1><a href="https://www.hindustantimes.com/">News</a><br>''',
    '''<h1>For Searching</h1><a href="https://www.google.com/">Google</a><br>
    ''']
    return HttpResponse(s)

def analyze(request):
    # Get the text
    djtext=request.POST.get('text','default')

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    # check which checkbox is on
    if removepunc =="on":
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == "  " and djtext[index+1]=="  "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc !="on" and newlineremover !="on" and extraspaceremover!="on" and fullcaps!="on" ):
        return HttpResponse("please select any operation and try again")


    return render(request, 'analyze.html', params)

#def capfirst(request):
 #   return HttpResponse("capitalize first <a href='/'>back</a>")

#def newlineremove(request):
 #   return HttpResponse("newlineremove <a href='/'>back</a>")

#def spaceremover(request):
 #   return HttpResponse("spaceremover <a href='/'>back</a>")

#def charcount(request):
 #   return HttpResponse("charcount <a href='/'>back</a>")

