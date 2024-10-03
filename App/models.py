from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission
from datetime import datetime

# Create your models here.
User = get_user_model()





class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    id_user = models.IntegerField()
    nickname =models.CharField(max_length=500,blank=True)
    bio = models.TextField(max_length=500, blank=True)
    faculty = models.CharField(max_length=500, blank=True)
    profileimage = models.ImageField(upload_to='profileImage', default='blank.png')
    is_verified = models.BooleanField(default=False)
    last_message = models.CharField(max_length=500, blank=True)
    
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):  
    user = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Image', blank=True)
    video = models.FileField(upload_to='video', blank=True)
    audio = models.FileField(upload_to='audio', blank=True)
    pdf = models.FileField(upload_to='pdf', blank=True)
    caption = models.TextField(max_length=5000)
    no_of_likes = models.IntegerField(default= 0)
    no_of_shares = models.IntegerField(default=0)
    no_of_commenters = models.IntegerField(default=0) 
    profileimage = models.ImageField(upload_to='post_profileImage', default='blank.png')
    created_at = models.DateTimeField(default=datetime.now) 
    favourites = models.FileField(upload_to='favourites', blank=True)
    favourites_text = models.CharField(max_length=50,blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user
    
class Comment(models.Model):
    name = models.CharField(max_length=50000000, null=True) 
    comment =  models.CharField(max_length=50000000, null=True)
    ids = models.CharField(max_length=50, null=True) 
    image = models.FileField(upload_to='Chat_Image', max_length=100, null=True)
    video = models.FileField(upload_to='Video_Image', max_length=100, null=True)
    profileimage = models.ImageField(default='blank.png', upload_to='comment')
    
    def __str__(self):
        return str(self.comment)

class LikePost(models.Model):
       name = models.CharField(max_length=500)
       ids = models.CharField(max_length=500)
       
       def __str__(self):
           return str(self.name)
    
class FollowersCount(models.Model):
    follower = models.CharField(max_length=500)
    user = models.CharField(max_length=500)
    def __str__(self):
        return self.user
    
class Favourite_post(models.Model):
    file = models.FileField(upload_to='Favourites', max_length=100)
    name = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.file)
 
class Notifications(models.Model):
    title = models.TextField()
    body = models.CharField(max_length=525)
    image = models.FileField(upload_to='announcement', max_length=255)
    video = models.FileField(upload_to='announcement', max_length=255)
    
class Group_comment(models.Model):
    name = models.CharField(max_length=50000000, null=True) 
    comment =  models.CharField(max_length=50000000, null=True)
    ids = models.CharField(max_length=50, null=True) 
    profileimage = models.ImageField(default='blank.png')
    group_name = models.CharField(max_length=50000000, null=True)
    
    def __str__(self):
        return str(self.comment)
    
class Message(models.Model):
    sender = models.CharField(max_length=50000000, null=True)
    receiver = models.CharField(max_length=50000000, null=True)
    profileimage = models.ImageField(default='blank.png')
    receiverId = models.CharField(max_length=50000000, null=True)
    senderId = models.CharField(max_length=50000000, null=True)
    message = models.CharField(max_length=50000000, null=True)
    image = models.FileField(upload_to='Image', max_length=100, null=True) 
    video = models.FileField(upload_to='Image', max_length=100, null=True) 
    def __str__(self):
        return str(self.sender)

 
 