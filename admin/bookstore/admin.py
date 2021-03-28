from django.contrib import admin
from . import models

# Register your models here.
class BookstoreAdminArea(admin.AdminSite):
    site_header = 'Bookstore Admin Page'

bookstore_site = BookstoreAdminArea('Bookstore Admin')    

admin.site.register(models.book)
bookstore_site.register(models.book)