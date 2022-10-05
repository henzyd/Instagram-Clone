from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreatePost(models.Model):
    caption = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(blank= True, upload_to='posts/')  ##### FIXME
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    edited_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.caption} by {self.owner}'

    def body_snippet(self):
        return self.body[:100] + '...'


# class Profile(models.Model):
#     user = models.OneToOneField(User, )