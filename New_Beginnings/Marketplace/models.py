from django.db import models

# Create your models here.
class User(models.Model):

    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    is_Student = models.BooleanField(default=True)
    degreeProgram = models.CharField(max_length=30, null=True, blank=True)
    office = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.FirstName +" "+self.LastName


class Tag(models.Model):
    text = models.CharField(max_length = 25)

    def __str__(self):
        return self.text

class Item(models.Model):
    item_name = models.CharField(max_length = 40)
    thumbnail = models.ImageField(blank=True)
    tag = models.ManyToManyField(Tag, blank = True)
    is_secondHand = models.BooleanField(default=False)
    is_academic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item_name
