from re import search
from django.shortcuts import render
import random
from . import util
import markdown
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def get_title(request,title):
    return render(request, "encyclopedia/titles.html",{
        "title": markdown.markdown(util.get_entry(title)), "title_page":title 
    })


def search(request):
    entries = util.list_entries()
    query = request.POST['q']
    if request.method == 'POST':
        for entry in entries:
            if (entry.upper()) .find(query.upper()) == 0:
                return render(request, "encyclopedia/titles.html",{
                    "title": markdown.markdown(util.get_entry(query)), "title_page":query 
                })
            else:
                entries_same = []
                query = query.upper()
                for entry in entries:
                    entry = entry.upper()
                    if query in entry:
                        entries_same.append(entry)
                return render(request, "encyclopedia/index.html", {
                    "entries": entries_same
            })    
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()

    })

def create_page(request):
    if request.method == "POST":
        name = request.POST['Name']
        text = request.POST['Text']
        util.save_entry(name,text)
        return render(request, "encyclopedia/titles.html",{
            "title": markdown.markdown(util.get_entry(name)), "title_page":name 
        })
                        
    return render(request,"encyclopedia/create_page.html")

def edit_title(request,title):                        
    return render(request, "encyclopedia/edit_title.html",{
        "title": markdown.markdown(util.get_entry(title)), "title_page":title 
    })

def random_page(request):
    entries = util.list_entries()
    num = random.randint(0,len(entries)-1)
    return  render(request, "encyclopedia/titles.html",{
        "title": markdown.markdown(util.get_entry(entries[num])), "title_page":entries[num] 
    })






    


    
    
    
