from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

#OneToOne relation with User model from Django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, blank=True)
    is_Student = models.BooleanField(default=True)
    degreeProgram = models.CharField(max_length=30, null=True, blank=True)
    office = models.CharField(max_length=30, null=True, blank=True)
    displayPic = models.FileField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def __str__(self):
        return self.FirstName +" "+self.LastName


class Tag(models.Model):
    text = models.CharField(max_length = 25)

    def __str__(self):
        return self.text

class Item(models.Model):
    profile = models.ForeignKey(Profile, null = True, blank=False)
    item_name = models.CharField(max_length = 40)
    thumbnail = models.ImageField(blank=True,null=True)
    tag = models.ManyToManyField(Tag, blank = True)
    is_secondHand = models.BooleanField(default=False)
    is_academic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    course_name = models.CharField(max_length=30,default="none",blank=True)

    def __str__(self):
        return self.item_name

class Offer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orig_post")
    is_Amount = models.BooleanField(default=False)
    amount_offer = models.IntegerField(default=0,null=True,blank=True)
    item_offer = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    reason = models.CharField(max_length = 200, blank=True)

    def __str__(self):
        return self.user.FirstName + self.user.LastName + ' offered on ' + self.item.item_name
