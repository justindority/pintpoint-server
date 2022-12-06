"""View module for handling requests about items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pintpointapi.models import Item, ItemType


class ItemView(ViewSet):
    """pintpoint item view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized item
        """

        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all items

        Returns:
            Response -- JSON serialized list of items
        """

        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized item instance
        """

        type = ItemType.objects.get(pk=request.data["itemType"])

        item = Item.objects.create(
            name=request.data["name"],
            price=request.data["price"],
            type=type

        )
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an item

        Returns:
            Response -- Empty body with 204 status code
        """

        item = Item.objects.get(pk=pk)
        item.name = request.data["name"]
        item.price = request.data["price"]
        item.type = ItemType.objects.get(pk=request.data["itemType"])
        
        item.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'type',)