from django.db import models
class Scenario(models.Model):
    order = models.IntegerField(default=0)
    content = models.CharField(max_length=256)
    
    def __str__(self):
        return self.content

class Category(models.Model):
    name = models.CharField('カテゴリ', max_length=100)
    def __str__(self):
        return self.name

class Term(models.Model):
    term = models.CharField(max_length=100)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', verbose_name="画像", null=True, blank=True)
    text = models.TextField()
    
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.term
