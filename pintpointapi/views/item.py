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


        if 'type' in request.query_params:
            type_to_int = int(request.query_params['type'])
            item_type = ItemType.objects.get(pk=type_to_int)
            items = items.filter(type=item_type)
        if 'active' in request.query_params:
            items = items.filter(active = True)

        serializer = ItemSerializer(items, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized item instance
        """

        type = ItemType.objects.get(pk=request.data["type"])

        if "maker" in request.data:
            maker = request.data["maker"]
        else:
            maker = ""

        item = Item.objects.create(
            name=request.data["name"],
            price=request.data["price"],
            maker = maker,
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

        if 'deactivate' in request.query_params:
            item.active = False
        elif 'reactivate' in request.query_params:
            item.active = True
        else:
            item.name = request.data["name"]
            item.price = request.data["price"]
            item.maker = request.data["maker"]
            item.type = ItemType.objects.get(pk=request.data["type"]["id"])
            
            
        item.save()
        serializer = ItemSerializer(item)

        return Response(serializer.data, status=status.HTTP_200_OK)

        



class ItemSerializer(serializers.ModelSerializer):
    """JSON serializer for items
    """
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'type', 'active', 'maker')
        depth = 1
        