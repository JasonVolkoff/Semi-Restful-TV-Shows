from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('show/<int:id>', views.show_info),
    path('show/<int:id>/edit', views.edit_show),
    path('show/<int:id>/destroy', views.destroy_show),
    path('show/<int:id>/update', views.update_show),
]
