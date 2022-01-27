from rest_framework import serializers
from app.models import Element


# class ElementDataSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ElementData
#         fields = ['label']

class ElementSerializer(serializers.ModelSerializer):
    # data = ElementSerializer(required=False)

    class Meta:
        model = Element
        fields = '__all__'




