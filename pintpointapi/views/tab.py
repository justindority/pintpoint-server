"""View module for handling requests about tabs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from datetime import date
from pintpointapi.models import Tab, Employee, Customer, Item, TabItems


class TabView(ViewSet):
    """pintpoint Tab view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single tab

        Returns:
            Response -- JSON serialized tab
        """


        tab = Tab.objects.get(pk=pk)
        serializer = TabSerializer(tab)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all tabs

        Returns:
            Response -- JSON serialized list of tabs
        """

        tabs = Tab.objects.all()


        if 'open' in request.query_params:
            tabs = tabs.filter(closed = False)
        if 'closed' in request.query_params:
            tabs = tabs.filter(closed=True)

        # for tab in tabs:
        #     if tab.items:
        #         for item in tab.items:
        #             temp_item = Item.objects.get(pk=item)

        serializer = TabSerializer(tabs, many=True) 
        return Response(serializer.data)


    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized tab instance
        """
        employee = Employee.objects.get(user=request.auth.user)

        tab = Tab.objects.create(
            employee=employee
        )
        serializer = TabSerializer(tab)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a tab

        Returns:
            Response -- Empty body with 204 status code
        """

        

        tab = Tab.objects.get(pk=pk)
        if request.data['customer']:
            tab.customer = request.data["customer"]
        tab.employee = Employee.objects.get(pk=request.data["employeeId"])
        tab.gratuity = request.data["gratuity"]
        tab.closed = request.data["closed"]
        
        tab.save()

        serialized = TabSerializer(tab)

        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        tab = Tab.objects.get(pk=pk)
        tab.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def additem(self, request, pk):
        """Post request to add an item to a tab"""
    
        TabItems.objects.create(
            item=Item.objects.get(pk=request.data['item']),
            tab=Tab.objects.get(pk=pk),
            timestamp=date.today()
            )
        return Response({'message': 'Item added'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def removeitem(self, request, pk):
        """delete request to remove an item from a tab"""
    
        item = Item.objects.get(pk=request.data['item'])
        tab = Tab.objects.get(pk=pk)
        multiple_items = (TabItems.objects.filter(item_id = request.data['item']) and TabItems.objects.filter(tab_id = pk))
        for thing in multiple_items:
            thing.delete()
            break

        return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
        



class TabSerializer(serializers.ModelSerializer):
    """JSON serializer for tabs
    """
    class Meta:
        model = Tab
        fields = ('id', 'employee', 'customer', 'gratuity', 'closed', 'items')
        depth = 2