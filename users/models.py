from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date
# Create your models here.
class Profile (models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
        
    is_doctor = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Appointment(models.Model):
    Category=(('Mental Health','Mental Health'),
    ('Heart Disease','Heart Disease'),
    ('Covid 19','Covid 19'),
    ('Imunization','Imunization '),)
    
    doctor=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    patient=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="messages")
    
    date = models.DateField(default=date.today)
    created=models.DateTimeField(auto_now_add=True)
    description= models.TextField(null=True,blank=True)
    select_category=models.CharField(max_length=200,choices=Category)
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True,editable=False)

    def __str__(self):
        return str(self.doctor)
    