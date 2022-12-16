"""View module for handling requests about employees"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pintpointapi.models import Employee
from datetime import date


class EmployeeView(ViewSet):
    """pintpoint Employee view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single employee

        Returns:
            Response -- JSON serialized employee
        """

        if 'me' in request.query_params:
            employee = Employee.objects.get(user=request.auth.user)
        else:
            employee = Employee.objects.get(pk=pk)


        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all employees

        Returns:
            Response -- JSON serialized list of employees
        """

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True) 
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized employee instance
        """

        user = User.objects.get(pk=request.data['user'])

        employee = Employee.objects.create(
            user=user,
            hourly_rate=request.data['hourlyRate'],
            hire_date=date.today()
            )

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for an employee

        Returns:
            Response -- Empty body with 204 status code
        """

        employee = Employee.objects.get(pk=request.data['id'])
        user = User.objects.get(pk=request.data['user_id'])

        employee.hourly_rate = request.data['hourly_rate']
        
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.username = request.data['username']
        user.is_staff = request.data['is_staff']

        employee.save()
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class EmployeeSerializer(serializers.ModelSerializer):
    """JSON serializer for employees
    """
    class Meta:
        model = Employee
        fields = ('id', 'user', 'hourly_rate', 'hire_date', 'term_date',)
        depth = 1