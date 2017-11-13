from django.conf.urls import url
from . import views as app_libri_views
from django.views.generic import ListView, DetailView
from .models import Book

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset = Book.objects.all().order_by("-data"),
        template_name = "lista_libri.html",
        paginate_by = 3), name="lista"),
        
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model=Book,
        template_name="libro_singolo.html"), name="singolo"),
    url(r'^contatti/$', app_libri_views.contatti, name="contatti"),
]
