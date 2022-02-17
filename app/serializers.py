from rest_framework import serializers
from app.models import Element, ElementManager

class ElementSerializer(serializers.ModelSerializer):


    class Meta:
        model = Element
        fields = '__all__'

    def create(self, validated_data):
        element = Element.objects.create_element(**validated_data)
        return element

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.href = validated_data.get('href', instance.href)
        instance.parent = validated_data.get('parent_id', instance.parent_id)
        instance.children = validated_data.get('children', instance.children)
        instance.children_list()
        instance.save()
        return instance







