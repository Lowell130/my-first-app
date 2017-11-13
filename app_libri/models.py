from django.db import models
from django.core.urlresolvers import reverse

class Book(models.Model):
    asin = models.CharField(max_length=250)
    titolo = models.CharField(max_length=250)
    autore = models.CharField(max_length=250)
    descrizione = models.TextField() 
    valutazione = models.CharField(max_length=10)  
    prezzo = models.CharField(max_length=10)
    link = models.URLField()
    image = models.URLField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.titolo

    
    def get_absolute_url(self):
        return reverse("singolo", kwargs={"id": self.id, "slug": self.slug})
     