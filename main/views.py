from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Show

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, 'shows.html', context)

def show_new(request):
    return render(request, 'add_show.html')

def show_create(request):
    new_show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['desc'])    
    return redirect(f'/shows/{new_show.id}')

def show_info(request, id):
    context = {
        "show" : Show.objects.get(id=id)
    }
    return render(request, 'show_info.html', context)

def show_edit(request, id):
    context = {
        "show" : Show.objects.get(id=id)
    }
    return render(request, 'edit_show.html', context)

def show_update(request, id):
    Show.objects.filter(id=id).update(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['desc'])
    show = Show.objects.get(id=id)
    show.save()
    return redirect(f'/shows/{id}')

def show_destroy(request, id):
    Show.objects.filter(id=id).delete()
    return redirect('/shows')