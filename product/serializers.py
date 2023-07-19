from rest_framework import serializers
from .models import *

class VariantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantImage
        fields = ('id', 'image')

class CategoryAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = ('name',)

class VariantSerializer(serializers.ModelSerializer):
    images = VariantImageSerializer(many=True)

    class Meta:
        model = Variant
        fields = ('id', 'color', 'ram', 'storage', 'size', 'price', 'images')

class SpecificationsSerializer(serializers.ModelSerializer):
    attribute = CategoryAttributeSerializer()

    class Meta:
        model = Specifications
        fields = ('attribute', 'value')

    def to_representation(self, instance):
        attribute_name = instance.attribute.name
        value = instance.value
        return {attribute_name: value}

class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)
    offer = serializers.StringRelatedField(many=True)
    highlights = serializers.StringRelatedField(many=True)
    specifications = SpecificationsSerializer(many=True, source='specifications_set')

    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'category', 'weight', 'length', 'width', 'height',
                  'variants', 'offer', 'highlights', 'specifications')
# product ^^^^^^^^^^^

#product catagory vvvvvvvvvv

class ProductCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name')

#category products list 

