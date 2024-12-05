from django.contrib import admin
from product.models import Category, CategoryImagess, Imagess,Product

class ProductImagesInline(admin.TabularInline):
    model=Imagess
    extra=5

class CategoryImagesInline(admin.TabularInline):
    model=CategoryImagess
    extra=5


class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','status']
    inlines=[CategoryImagesInline]


class ProductAdmin(admin.ModelAdmin):
    list_display=['title','status','image_tag','price']
    inlines=[ProductImagesInline]
    readonly_fields=('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display=['title']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Imagess,ImagesAdmin)
# Register your models here.
