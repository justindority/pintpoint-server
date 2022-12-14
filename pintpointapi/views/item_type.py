"""View module for handling requests about item types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from pintpointapi.models import Tab, Employee, Customer, Item, ItemType


class ItemTypeView(ViewSet):
    """pintpoint item type view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single item type

        Returns:
            Response -- JSON serialized item type
        """

        item_type = ItemType.objects.get(pk=pk)
        serializer = ItemTypeSerializer(item_type)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all item types

        Returns:
            Response -- JSON serialized list of item types
        """

        item_types = ItemType.objects.all()


        serializer = ItemTypeSerializer(item_types, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized item type instance
        """

        item_type = ItemType.objects.create(
            type=request.data['itemType']
        )

        serializer = ItemTypeSerializer(item_type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an item_type

        Returns:
            Response -- Empty body with 204 status code
        """

        

        item_type = ItemType.objects.get(pk=pk)
        item_type.type = request.data["type"]
        
        item_type.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        item_type = ItemType.objects.get(pk=pk)
        item_type.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)





class ItemTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for item types
    """
    class Meta:
        model = ItemType
        fields = ('id', 'type')