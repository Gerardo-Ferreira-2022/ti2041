from django.db import models
#from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Agrega una relación con el usuario


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    def __str__(self):
        return "comentario de {name} {content}"
