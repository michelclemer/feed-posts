from django.contrib import admin

from recipes.models import Recipe, Category


class CategoryAdmin(admin.ModelAdmin):
    ...


# Primeira forma de registrar via decorator
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


# Segunda forma de registrar via chamada da função
admin.site.register(Category, CategoryAdmin)
