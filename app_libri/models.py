from django.db import models
from django.forms import ModelForm
from django.core.urlresolvers import reverse

"""
blank=True significa che accetta il valore "vuoto" che viene salvato dall'admin.
null=True e' relativo al database e significa che accetta il "non valore"
Purtroppo in Django il model e l'admin sono molto legati quando l'admin e' in realta' solo 
un presentation layer e non dovrebbe avere niente a che fare con la definizione dei modelli
"""

class Book(models.Model):
    asin = models.CharField(max_length=250)
    titolo = models.CharField(max_length=250)
    autore = models.CharField(max_length=250)
    descrizione = models.TextField() 
    valutazione = models.CharField(max_length=10)  
    prezzo = models.CharField(max_length=10)
    link = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.titolo

    
    def get_absolute_url(self):
        return reverse("singolo", kwargs={"id": self.id, "slug": self.slug})


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['asin', 'titolo', 'autore', 'descrizione', 'valutazione', 'prezzo', 'link', 'image', 'data', 'slug']