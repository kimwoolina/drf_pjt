from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender_choices = [
        ("m", "남성"),
        ("f", "여성")
    ]
    
    nickname = models.CharField(max_length=50, unique=True)
    birth = models.DateField()
    
    #선택필드 (null=True), (default="")
    gender = models.CharField(max_length=1, choices=gender_choices, null=True, blank=True)
    introduction = models.TextField(default="")
    
    