from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from car.models import Car
from car.api.serializers import (
    BaseCarSerializer,
    CarSerializer,
    CarUpdateSerializer,
    CarDeleteSerializer,
)


class CarList(generics.ListAPIView):
    """
    GET: List all cars.

    ** Optional query parameters:-
        i) name = category, value = True
        ii) name = engine, value = True
    """

    queryset = Car.objects.all().order_by("id")
    serializer_class = BaseCarSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def list(self, request):
        remove_fields = ["category", "engine"]

        category = self.request.query_params.get("category")
        engine = self.request.query_params.get("engine")

        if category:
            remove_fields.remove("category")

        if engine:
            remove_fields.remove("engine")

        queryset = self.get_queryset()
        serializer = self.serializer_class(
            queryset, many=True, remove_fields=remove_fields
        )

        return Response(serializer.data)


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

    * Requires `id` of the instance as query parameter.
    ** Optional query parameters:-
        i) name = category, value = True
        ii) name = engine, value = True
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
        category = self.request.query_params.get("category")
        engine = self.request.query_params.get("engine")

        if not pk:
            error = "Please provide a valid `id` query parameter in the URL!"
            raise ValidationError(error)

        remove_fields = ["category", "engine"]

        if category:
            remove_fields.remove("category")

        if engine:
            remove_fields.remove("engine")

        car = self.get_object(pk)
        serializer = self.serializer_class(car, remove_fields=remove_fields)
        return Response(serializer.data)


class CarUpdate(APIView):
    """
    POST: Update a car instance.

    * Requires `id` of the instance in POST data.
    """

    serializer_class = CarUpdateSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.get_object(serializer.validated_data["id"])
        serializer = CarSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CarDelete(APIView):
    """
    POST: Delete a car instance.

    * Requires `id` of the instance in POST data.
    """

    serializer_class = CarDeleteSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve and delete instance
        instance = self.get_object(serializer.validated_data.get("id"))
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
