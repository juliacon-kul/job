from django.shortcuts import render
from app.models import Element, ElementManager
from app.serializers import ElementSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.http import Http404


class ElementView(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        element = Element.objects.all()
        for i in element:
            i.children = i.nums_from_string()
        serializer = ElementSerializer(element, many = True)
        return Response(serializer.data)

    def post(self, request):
        element = request.data.get('element')
        element['children'] = []
        if (type(data['parent_id']) is int and data['parent_id'] > 0):
            if Element.objects.filter(pk=element['parent_id']).exists():
                serializer = ElementSerializer(data = element)
                if serializer.is_valid(raise_exception=True):
                    element_saved = serializer.save()
                return Response({"id":"{}".format(element_saved.id),
                                 "parent_id":"{}".format(element_saved.parent_id.id),
                                 "href":"{}".format(element_saved.href),
                                 "label":"{}".format(element_saved.label)
                            })
            else:
                return Response({
                    "Элемент с таким родительским id'{}' не существует"
                })
        else: return Response({
                    "Parent_id должен иметь тип данных int"
                })

    def put(self, request, pk):
        if Element.objects.filter(pk = pk).exists():
            saved_element = Element.objects.get(pk = pk)
            data = request.data.get('element')
            if (type(data['parent_id']) is int and data['parent_id'] > 0):
                if Element.objects.filter(pk = data['parent_id']).exists():
                    serializer = ElementSerializer(instance=saved_element, data=data, partial=True)
                    if serializer.is_valid(raise_exception=True):
                        saved_element = serializer.save()
                    return Response({
                        "Элемент с id'{}' успешно изменен".format(saved_element.id)
                    })
                else:return Response({
                        "Элемент с таким родительским id'{}' не существует"
                    })
            else:
                return Response({
                    "Parent_id должен иметь тип данных int и быть больше 0"
                })
        else: return Response("Элемент с “id”: '{}' не существует, запрос не был выполнен".format(pk), status = 404)

    def delete(self, request, pk):
        try:
            element = Element.objects.get(pk = pk)
            if element.id != 1:
                element.children_list_delete()
                element.delete()
                return Response({
                    "Элемент с id'{}' удален".format(pk)
                })
            else: return Response({
                    "Элемент с id=1 нельзя удалить"})
        except Element.DoesNotExist:
            return Response("Элемент с “id”: '{}' не существует, запрос не был выполнен".format(pk), status=404)






