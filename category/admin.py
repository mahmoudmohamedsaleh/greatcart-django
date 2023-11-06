from django.contrib import admin

from category import models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display = ('category_name', 'slug')


admin.site.register(models.category,CategoryAdmin)

# Register your models here.
