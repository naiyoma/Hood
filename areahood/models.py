from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import MinValueValidator,MaxValueValidator


@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name=models.CharField(max_length = 60)
    neighbourhood_location = models.CharField(max_length = 90) 
    occupants_count=models.CharField(max_length = 70)
    # admin = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-id']
 
    def __str__(self):
        return self.neighbourhood_name
    
    def create_neighbourhood(self):
        self.save()

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    def update_neighbourhood(self):
        self.save()

    def update_occupants(self):
        self.save()

    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        neighbourhood = cls.objects.get(id=neighbourhood_id)
        return neighbourhood

class Location(models.Model):
    location = models.CharField(max_length= 30)
    
    def __str__(self):
        return self.location


class Profile(models.Model):
    username = models.CharField(max_length = 30)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    profile_image = models.ImageField(upload_to = 'images/')
    email = models.EmailField(max_length=70,blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True)
    location = models.ForeignKey(Location,null=True)
    
    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    def update_description(self):
        self.save()

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(username__icontains=search_term)
        return profiles

    @property
    def photo_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url


class Post(models.Model):
    image = models.ImageField(upload_to = 'images/',null=True)  
    post = models.CharField(max_length = 30)
    post_description = models.CharField(max_length = 40,blank=True)
    profile = models.ForeignKey(Profile,null=True)
    user = models.ForeignKey(User,null=True)
    posted_time = models.DateTimeField(auto_now_add=True,null=True)
    link = models.URLField(max_length = 80,null=True)

    class Meta:
        ordering = ['-id']
 
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.save()

    def update_caption(self):
        self.save()

    def average_rating(self):
        all_ratings =list(map(lambda x: x.rating, self.review_set.all()))
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.image_name

    
class Business(models.Model):  
    business_name = models.CharField(max_length = 130)
    business_email = models.EmailField(max_length=70,blank=True)
    profile = models.ForeignKey(Profile,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True)
    user = models.ForeignKey(User,null=True)
    posted_time = models.DateTimeField(auto_now_add=True,null=True)
    product = models.ImageField(upload_to = 'images/',null=True) 
   
    class Meta:
        ordering = ['-id']
 
    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.save()

    def update_business(self):
        self.save()

    def create_business(self):
        self.save()   

    @classmethod
    def find_business(cls,business_id):
        business = cls.objects.get(id=business_id)
        return business                   



   

        
