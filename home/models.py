from django.db import models
from django.utils.safestring import mark_safe

class Settings(models.Model):
        STATUS= (('True','Evet'),
                 ('False','Hayır'),)
        title=models.CharField(blank=True, max_length=100)
        keywords=models.CharField(blank=True, max_length=100)
        description=models.CharField(blank=True, max_length=250)
        company=models.CharField(blank=True, max_length=100)
        adress=models.CharField(blank=True, max_length=250)
        phone=models.CharField(blank=True, max_length=15)
        fax=models.CharField(blank=True, max_length=15)
        e_mail=models.CharField(blank=True, max_length=50)
        smtpserver=models.CharField(blank=True, max_length=100)
        smtpemail=models.CharField(blank=True, max_length=60)
        smtppassword=models.CharField(blank=True, max_length=20)
        smtpport=models.CharField(blank=True, max_length=20)
        facebook=models.CharField(blank=True, max_length=60)
        instagram=models.CharField(blank=True, max_length=40)
        contact=models.CharField(blank=True,max_length=100)
        aboutus=models.TextField(blank=True)
        reference=models.TextField(blank=True)
        icon=models.ImageField(blank=True,upload_to='images/')
        status=models.CharField(blank=True, max_length=20,choices=STATUS)
        create_at=models.DateTimeField(auto_now_add=True)
        upload_at=models.DateTimeField(auto_now=True)
        def __str__(self):
            return self.title  
        def image_tag(self):
            if self.icon and hasattr(self.icon, 'url'):
                return mark_safe('<img src="{}" width="69" height="50"/>'.format(self.icon.url))
            else:
                return "Resim Yüklenmedi"
        image_tag.short_description = 'Image'

# Create your models here.
