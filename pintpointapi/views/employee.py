"""View module for handling requests about employees"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from pintpointapi.models import Employee


class EmployeeView(ViewSet):
    """pintpoint Employee view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single employee

        Returns:
            Response -- JSON serialized employee
        """

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


    def update(self, request, pk):
        """Handle PUT requests for an employee

        Returns:
            Response -- Empty body with 204 status code
        """

        employee = Employee.objects.get(pk=pk)
        employee.employee = Employee.objects.get(pk=request.data["employee_id"])
        employee.gratuity = request.data["gratuity"]
        employee.closed = request.data["closed"]
        
        employee.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        



class EmployeeSerializer(serializers.ModelSerializer):
    """JSON serializer for employees
    """
    class Meta:
        model = Employee
        fields = ('id', 'user', 'hourly_rate', 'hire_date', 'term_date',)