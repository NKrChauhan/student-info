from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import re

def get_links(link):

    return_links = []

    r = requests.get(link)

    soup = BeautifulSoup(r.content, "lxml")

    if r.status_code != 200:
        return ['something went wrong , is it a valid url']
    else:
        for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
            return_links.append(link.get('href'))

    return return_links

def linkListView(request,*args,**kwargs):
    query=request.GET.get('url',None)
    data={
        'links':['<Enter the link in the box>',]
    }
    if query is not None:
        data = {
            'links':get_links(query)
        }
    return render(request,'linksgrab/linksview.html',data)