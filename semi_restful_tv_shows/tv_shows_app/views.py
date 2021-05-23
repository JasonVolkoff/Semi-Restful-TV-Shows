from django.shortcuts import render, redirect
from .models import Show
# Create your views here.


def shows(request):  # path('shows', views.shows),
    context = {
        "shows": Show.objects.all(),
    }
    return render(request, 'shows.html', context)


def new_show(request):  # path('shows/new', views.new_show),
    return render(request, 'new_show.html')


def create_show(request):  # path('shows/create', views.create_show),
    if request.method == "POST":
        new_show = Show.objects.create(
            title=request.POST["title"],
            network=request.POST["network"],
            release_date=request.POST["releaseDate"],
            description=request.POST["description"]
        )
        new_show.save()
    return redirect(f'/shows/{new_show.id}')


def show_info(request, id):  # path('shows/<int:id>', views.show_info),
    context = {
        "this_show": Show.objects.get(id=id),
    }
    return render(request, 'show_info.html', context)


def edit_show(request, id):  # path('shows/<int:id>/edit', views.edit_show),
    context = {
        "this_show": Show.objects.get(id=id),
    }
    return render(request, 'edit_show.html', context)


def destroy_show(request, id):  # path('shows/<int:id>/destroy', views.destroy_show),
    delete_show = Show.objects.get(id=id)
    delete_show.delete()
    return redirect('/shows')


def update_show(request, id):  # path('shows/<int:id>/update', views.update_show),
    if request.method == "POST":
        update_show = Show.objects.get(id=id)
        update_show.title = request.POST["title"]
        update_show.network = request.POST["network"]
        update_show.release_date = request.POST["releaseDate"]
        update_show.description = request.POST["description"]
        update_show.save()
    return redirect(f'/shows/{id}')
