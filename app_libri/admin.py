from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
     list_display = ["__str__","data", "asin", "prezzo", "autore"]
     list_filter = ["data"]
     search_fields = ["asin", "titolo"]
     prepopulated_fields = {"slug": ("titolo",)}

     class Meta:
         model = Book


admin.site.register(Book, BookAdmin)
