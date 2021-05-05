from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from car.models import Car
from car.api.serializers import BaseCarSerializer, CarSerializer


class CarList(generics.ListAPIView):
    """
    GET: List all cars.
    """

    queryset = Car.objects.all().order_by("id")
    serializer_class = BaseCarSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class CarCreate(generics.CreateAPIView):
    """
    POST: Create a new car.
    """

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class CarDetail(APIView):
    """
    GET: Retrieve a car instance.

    * Requires ``id`` of the instance as query parameter.
    """

    serializer_class = BaseCarSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request):
        pk = self.request.query_params.get("id")

        if not pk:
            error = "Please provide a valid `id` query parameter in the URL!"
            raise ValidationError(error)

        car = self.get_object(pk)
        serializer = self.serializer_class(car)
        return Response(serializer.data)


class CarUpdate(APIView):
    """
    PUT: Update a car instance.

    * Requires ``id`` of the instance as query parameter.
    """

    serializer_class = CarSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def put(self, request):
        pk = self.request.query_params.get("id")

        if not pk:
            error = "Please provide a valid `id` query parameter in the URL!"
            raise ValidationError(error)

        car = self.get_object(pk)
        serializer = self.serializer_class(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            raise ValidationError(serializer.errors)


class CarDelete(APIView):
    """
    DELETE: Delete a car instance.

    * Requires ``id`` of the instance as query parameter.
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def delete(self, request):
        pk = self.request.query_params.get("id")

        if not pk:
            error = "Please provide a valid `id` query parameter in the URL!"
            raise ValidationError(error)

        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
