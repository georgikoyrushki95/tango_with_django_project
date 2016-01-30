from django.contrib import admin
from models import Category, Page

# add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)