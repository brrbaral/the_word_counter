from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'hi_there':'This is django-from html'})

def about(request):
    return render(request,'about.html')

def count(request):
    finaltext=request.GET['fulltext']
    worldlist=finaltext.split( )

    worddictionary={}
    for word in worldlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add to the dictionary
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'finaltext':finaltext,'count':len(worldlist),'sortedwords':worddictionary.items()})
	#.items() is for converting the dictionary into list
	