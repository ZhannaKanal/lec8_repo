from django.db import models
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    picture=models.ImageField(default='default value')
    author=models.CharField(max_length=30, default='anonymous')
    email=models.EmailField(blank=True)
    describe=models.TextField(default='DataFlair Django tutorials')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Мақала"
        verbose_name_plural="Мақалалар"
        ordering=['-author','title']

class Categories(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    picture=models.ImageField(default='default value')
    describe=models.TextField(default='DataFlair Django tutorials')

class Mosts(models.Model):
    title=models.CharField(max_length=255, verbose_name="Takyryp")
    is_published=models.BooleanField(default=True,verbose_name="Wyggarylym")
    

class Tosts(models.Model):
    title=models.CharField(max_length=255, verbose_name="Takyryp")
    is_published=models.BooleanField(default=True,verbose_name="Wyggarylym")  
    slug=models.SlugField(max_length=255, verbose_name='URL',unique=True, db_index=True)  
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

   
class Poster(models.Model):
    esim = models.CharField(max_length=255, verbose_name="Esimi",default='') 
    teg=models.TextField(blank=True,default='', verbose_name="Tegi")
    age = models.IntegerField(verbose_name='Zhasy',default=18)
    email=models.EmailField(blank=True,default='@gmail.com',verbose_name='Elektrondyk poshta')
    image = models.ImageField(default='default value',upload_to='user_gallery', blank=True, null=True,verbose_name='3*4 suret')
    slug=models.SlugField(max_length=255,default='', unique=True, db_index=True, verbose_name="URL")
    is_published=models.BooleanField(default=False, verbose_name="Kelisim")

    REQUIRED_FIELDS = ['esim',]
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
   
    
    