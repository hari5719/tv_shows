from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages


def index(request):


    return render(request, "tvshow_app/index1.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title= request.POST['title'],network=request.POST['network'],date=request.POST['date'],desc=request.POST['desc'])
        print(new_show)
        request.session['id'] = new_show.id
        return redirect("/shows/"+ str(request.session['id'])) # need to add ID 

def info(request,id):
    query =Show.objects.get(id = id)
    content = {
        "the_show": query,
            
    }
    return render(request, "tvshow_app/index2.html", content)


def edit(request, id):
    request.session['id'] = id
    query = Show.objects.get(id = id)

    content = {
        "show_edit": query,
    }

    return render(request, "tvshow_app/index4.html", content)

def save_edit(request, id):
    errors = Show.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/"+request.session['id']+"/edit")
    else:
        show_update = Show.objects.get(id = id)
        show_update.title = request.POST['title']
        show_update.network=request.POST['network']
        show_update.date=request.POST['date'] 
        show_update.desc=request.POST['desc']
        show_update.save()
        return redirect("/shows/"+request.session['id']+"/edit")


def delete(request, id):
    delete_show = Show.objects.get(id = id)
    delete_show.delete()
    return redirect("/shows")


def index3(request):
    
    content = {
        "all_shows": Show.objects.all(),
            
    }
    return render(request, "tvshow_app/index3.html", content)