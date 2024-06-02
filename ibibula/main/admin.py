from django.contrib import admin

from main.models import Categories, Subcategories, Services



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
 

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}