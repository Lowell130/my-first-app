import csv,sys,os
project_dir = 'C: \\Utenti\\Stew\Desktop\\root'

#sys.patch.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'progetto1.settings'

import django
django.setup()

from app_libri.models import Book

data = csv.reader(
	open('test_import.csv'), delimiter=",")




#RIVEDERE LE POSIZIONE DELLE COLONNE PERCHé NON SI TROVANO    

for row in data:
    if row[0] != 'ASIN':
        post = Book()
        post.asin = row[0]
        post.titolo = row[1]
        post.autore = row[2]
        post.descrizione = row[4]
        post.valutazione = row[6]
        post.prezzo = row[7]
        post.link = row[21]
        post.image = row[22]
        post.save()

       
       
       

    
