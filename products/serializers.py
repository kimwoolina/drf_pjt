from rest_framework import serializers
from .models import Product, Products, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
        
    # instance : Product object임 
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        
        # category_name = ""
        # if instance.category:
        #     category_name = instance.category.name
        
        # 위 코드를 이렇게 한줄로 축약 가능
        # category_name = instance.category.name if instance.category else "" 
        
        ret["category"] = CategorySerializer(instance.category).data
        
        return ret
        
