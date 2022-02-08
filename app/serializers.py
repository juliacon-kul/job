from rest_framework import serializers
from app.models import Element

# class ElementDataSerializer(serializers.Serializer):
#     label = serializers.CharField(max_length=255)
#     id = serializers.IntegerField(read_only=True)
# #
#     class Meta:
#         model = ElementData
#         fields = ['label','id']

class ElementSerializer(serializers.Serializer):

    child = serializers.PrimaryKeyRelatedField(queryset=Element.objects.all())
    href = serializers.CharField(max_length=255)
    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField(max_length=255)

    def create(self, validated_data):
        element = Element.objects.create(**validated_data)

        return element


    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.href = validated_data.get('href', instance.href)
        instance.parent = validated_data.get('child', instance.child)
        instance.save()
        return instance







