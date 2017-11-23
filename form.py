from django import forms

# form per verifica campi CSV

class BookForm(forms.Form):
    
    #numero identificativo di 10 cifre alfanumeriche
    asin = forms.CharField(max_length=10)

    titolo = forms.CharField(max_length=150)

    autore = forms.CharField(max_length=100)
    
    descrizione = forms.CharField()
    
    #numero con virgola es. 4,5 o intero 5 (da 0 a 5)
    valutazione = forms.DecimalField()

    #prezzo indicato come sempre come intero o decimale
    prezzo = forms.DecimalField()

    # link diretto al prodotto, deve esserci per forza
    link = forms.URLField(null=False, blank=False)

    #link diretto all'immagine
    image = forms.ImageField(null=True, blank=True)

    data = forms.DateTimeField(auto_now=False, auto_now_add=True)

    slug = forms.SlugField(null=True, blank=True)
