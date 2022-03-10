from rest_framework import serializers
from app.models import Element, ElementManager

class ElementSerializer(serializers.ModelSerializer):

    children = serializers.ListField(allow_empty=True)
    class Meta:
        model = Element
        fields = ('id','href', 'parent_id', 'label', 'children')

    def create(self, validated_data):
        element = Element.objects.create_element(**validated_data)
        return element

    def update(self, instance, validated_data):
        if validated_data.get('parent_id') not in Element.objects.all():
            return "Нет такого parent_id"
        else:
            if instance.parent_id != validated_data.get('parent_id'):
                instance.children_list_delete()
                instance.label = validated_data.get('label', instance.label)
                instance.href = validated_data.get('href', instance.href)
                instance.parent_id = validated_data.get('parent_id', instance.parent_id)
                instance.save()
                instance.children_list_update()
            else:
                instance.label = validated_data.get('label', instance.label)
                instance.href = validated_data.get('href', instance.href)
                instance.parent_id = validated_data.get('parent_id', instance.parent_id)
                instance.save()

            return instance







