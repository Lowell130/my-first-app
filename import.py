import csv,sys,os
project_dir = 'C: \\Utenti\\Stew\Desktop\\root'

#sys.patch.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'progetto1.settings'

import django
django.setup()

from app_libri.models import Book

data = csv.reader(
	open('test_import.csv'), delimiter=",")




#DA RIVEDERE LE POSIZIONE DELLE COLONNE PERCHé NON CORRISPONDONO CON QUELLE DEL FILE CSV

for row in data:
    if row[0] != 'ASIN':
        post = Book()
        post.asin = row[0]
        post.titolo = row[1]
        post.autore = row[2]
        post.descrizione = row[4]
        post.valutazione = row[6]
        post.prezzo = row[9]
        post.link = row[24]
        post.image = row[25]
        post.save()

       
       
       

    
