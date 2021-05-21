from django.shortcuts import render, redirect
from .models import Show, Network
# Create your views here.


def shows(request):  # path('shows', views.shows),
    context = {
        "shows": Show.objects.all(),
        "networks": Network.objects.all()
    }
    return render(request, 'shows.html', context)


def new_show(request):  # path('shows/new', views.new_show),
    return render(request, 'new_show.html')


def create_show(request):  # path('shows/create', views.create_show),
    if request.method == "POST":
        Show.objects.create(
            title=request.post["title"],
            release_date=request.post["releaseDate"]
        )
        # check if user input Network exists, then creates one if not existing
        if not Network.objects.filter(name=request.post["name"]):
            Network.objects.create(
                name=request.post["name"]
            )
        # establish relationship between Network and Show
        Show.objects.last.networks.add(
            Network.objects.filter(name=request.post["name"]))
    return redirect(f'/show/{Show.objects.last}')


def show_info(request, show_id):  # path('show/<int:id>', views.show_info),
    pass


def edit_show(request, show_id):  # path('show/<int:id>/edit', views.edit_show),
    pass


def destroy_show(request, show_id):  # path('show/<int:id>/destroy', views.destroy_show),
    pass


def update_show(request, show_id):  # path('show/<int:id>/update', views.update_show),
    pass
