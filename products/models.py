from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Fruit"), # (DB에 저장되는 값, 유저에게 보여지는 값)
        ("V", "Vegetable"),
        ("M", "Meat"),
        ("O", "Other"),
    )
    name = models.CharField(max_length=30)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name