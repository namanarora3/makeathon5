from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    CHOICES = (
        ('street','Street'),
        ('footpath', 'Footpath'),
        ('washroom', 'washroom')
    )
    name = models.CharField(max_length=100)
    category = models.CharField(choices=CHOICES,max_length=100)
    assigned = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='task_images',null=True,blank=True)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-assigned']