from django.contrib import admin

from book.models import *

# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(PeopleInfo)


