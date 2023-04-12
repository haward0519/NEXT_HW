from django.db import models



# Create your models here.

class Article (models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()
    dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
   article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()

   def __str__(self):
       return self.content

class Recomment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='recomments')
    content = models.TextField()

    def __str__(self):
        return self.content