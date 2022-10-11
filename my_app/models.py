from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreatePost(models.Model):
    caption = models.CharField(max_length=100, blank=False)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='posts/', blank=True)  ##### FIXME
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    edited_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return f'{self.caption} by {self.owner}'

    def body_snippet(self):
        if len(self.body) <= 100:
            return self.body
        else:
            return self.body[:100] + '...'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='profiles/default_teamyy.jpg', upload_to='profiles/', blank=True)

    def __str__(self) -> str:
        return f'{self.user}'

    @property
    def profile_imgURL(self):
        try:
            url = self.profile_img.url
            print('sdfdfd')
            print(url)
        except:
            print('sommmkf')
            url = ''
        return url

