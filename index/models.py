from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return F"{self.name}"
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
class Products(models.Model):
    title =models.CharField(max_length=30 , verbose_name="سربرگ")
    name =models.CharField(max_length=30 , verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    link_img = models.CharField(max_length=60 , verbose_name="اسم عکس" , null=True)
    category = models.ManyToManyField(Category ,verbose_name="دسته بندی ها")
    slug = models.SlugField(default="" , null=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
class Comments(models.Model):
    name = models.CharField(max_length=30 ,  verbose_name="نام کاربری")
    email =models.CharField(max_length=30 , verbose_name="ایمیل")
    message =  models.TextField(verbose_name="پیام")