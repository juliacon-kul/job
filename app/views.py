from django.shortcuts import render
from app.models import Element, ElementManager
from app.serializers import ElementSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404

class ElementView(APIView):
    permission_classes = [permissions.AllowAny,]

    def get(self, request):
        element = Element.objects.all()
        serializer = ElementSerializer(element, many = True)
        return Response({"element":serializer.data})

    def post(self, request):
        element = request.data.get('element')
        serializer = ElementSerializer(data = element)
        if serializer.is_valid(raise_exception=True):
            element_saved = serializer.save()
        return Response({"success":"Element '{}' created succesfully".format(element_saved.label)})

    def put(self, request, pk):
        saved_element = get_object_or_404(Element.objects.all(), pk = pk)
        data = request.data.get('element')
        serializer = ElementSerializer(instance = saved_element, data = data, partial = True)
        if serializer.is_valid(raise_exception=True):
            element_saved = serializer.save()
        return Response({
            "success":"Element'{}' updated successfully".format(element_saved.label)
        })
    def delete(self, request, pk):
        element = get_object_or_404(Element.objects.all(), pk = pk)
        element.children_list_delete()
        element.delete()
        return Response({
            "message": "Element'{}' has been deleted".format(pk)
        },status = 204)


# class ElementDataView(APIView):
#     permission_classes = [permissions.AllowAny, ]
#
#     def get(self, request):
#         elementdata = ElementData.objects.all()
#         serializer = ElementDataSerializer(elementdata, many=True)
#         return Response({"data": serializer.data})
#
#     def post(self, request):
#         elementdata = request.data.get('data')
#         serializer = ElementSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             elementdata_saved = serializer.save()
#         return Response({"success": "Element '{}' created succesfully".format(elementdata_saved.label)})
#
#     def put(self, request, pk):
#         saved_elementdata = get_object_or_404(ElementData.objects.all(), pk=pk)
#         data = request.data.get('data')
#         serializer = ElementDataSerializer(instance=saved_elementdata, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             elementdata_saved = serializer.save()
#         return Response({
#             "success": "Element'{}' updated successfully".format(elementdata_saved.label)
#         })

    # def delete(self, request, pk):
    #     elementdata = get_object_or_404(ElementData.objects.all(), pk=pk)
    #     elementdata.delete()
    #     return Response({
    #         "message": "Element'{}' has been deleted".format(pk)
    #     }, status=204)

# Create your views here.
# class ElementList(generics.ListCreateAPIView):
#     queryset = Element.objects.all()
#     serializer_class = ElementSerializer
#
# # class ElementDataList(generics.ListCreateAPIView):
# #     queryset = ElementData.objects.all()
# #     serializer_class = ElementDataSerializer

# class ElementDetail(generics.RetrieveAPIView):
#     queryset = Element.objects.all()
#     serializer_class = ElementSerializer


