from django.db import models
from django.utils.safestring import mark_safe

class Category(models.Model):
    STATUS= (('True','Evet'),
     ('False','Hayır'),)

    title=models.CharField(max_length=100)
    keywords=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=20,choices=STATUS)
    slug=models.SlugField()
    parent=models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image and hasattr(self.image,'url'):
            return mark_safe('<img src="{}" width="65" height="60"/>'.format(self.image.url))
        else:
            return 'resim yüklenemedi'
    image_tag.short_description='Image'
    
class Product(models.Model):
    STATUS= (('True','Evet'),
                ('False','Hayır'),)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    keywords=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to='images/')
    price=models.FloatField()
    amount=models.IntegerField()
    detail=models.TextField()
    status=models.CharField(max_length=20,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    upload_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.image and hasattr(self.image, 'url'):
            return mark_safe('<img src="{}" width="69" height="50"/>'.format(self.image.url))
        else:
            return "Resim Yüklenmedi"
    image_tag.short_description = 'Image'
    

class Imagess(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=65)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image and hasattr(self.image,'url'):
            return mark_safe('<img src="{}" width="65" height="60"/>'.format(self.image.url))
        else:
            return 'resim yüklenemedi'
    image_tag.short_description='Image'
    
class CategoryImagess(models.Model):

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=65)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        if self.image and hasattr(self.image,'url'):
            return mark_safe('<img src="{}" width="65" height="60"/>'.format(self.image.url))
        else:
            return 'resim yüklenemedi'
    image_tag.short_description='Image'