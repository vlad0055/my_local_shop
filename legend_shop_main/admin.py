from django.contrib import admin

from .models import Product



# class ProductAdmin(admin.ModelAdmin):
# 	list_display=('name',"picture","healthy","date")
# 	list_display_links=[]
# 	search_fields=['name']

admin.site.register(Product)
# admin.site.register(ProductAdmin)


# verbose_name="Мой магазин"