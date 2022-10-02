from dataclasses import field
from pyexpat import model
from unicodedata import category
from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class SimplePostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        exclude = ('text', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
