"""View module for handling requests about customers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pintpointapi.models import Customer


class CustomerView(ViewSet):
    """pintpoint Customer view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single customer

        Returns:
            Response -- JSON serialized customer
        """

        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all customers

        Returns:
            Response -- JSON serialized list of customers
        """

        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True) 
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized customer instance
        """

        customer = Customer.objects.create(
            name=request.data["name"]
        )
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        """Handle PUT requests for an customer

        Returns:
            Response -- Empty body with 204 status code
        """

        customer = Customer.objects.get(pk=pk)
        customer.name = request.data["name"]        
        customer.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class CustomerSerializer(serializers.ModelSerializer):
    """JSON serializer for customers
    """
    class Meta:
        model = Customer
        fields = ('id', 'name',)