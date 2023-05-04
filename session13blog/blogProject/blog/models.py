from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article (models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    article = models.TextField()
    dt = models.DateTimeField(auto_now=True)
    update_dt = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=True)

    class Meta:
        verbose_name = "MyPost"
        verbose_name_plural = "MyPosts"
        ordering = ('-update_dt', 'author')    

    def __str__(self):
        return f'{self.pk}. {self.title}'

class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_comments", null=True)
   dt = models.DateTimeField(auto_now_add=True)
   update_dt = models.DateTimeField(auto_now=True)

   class Meta:
        verbose_name = "MyComment"
        verbose_name_plural = "MyComments"
        ordering = ('-dt', 'article', 'author')

   def __str__(self):
        return f'{self.pk}. {self.content}'
