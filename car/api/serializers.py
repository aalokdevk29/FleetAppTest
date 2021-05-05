from rest_framework import serializers

from car.models import Car, Category, Manufacturer


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ["id", "name"]
        read_only_fields = ["id"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        read_only_fields = ["id"]


class BaseCarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "category",
            "powertrain",
            "max_passenger",
            "manufacturing_year",
            "registration",
            "created",
            "updated",
        ]
        read_only_fields = [
            "id",
            "created",
            "updated",
        ]


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "category",
            "powertrain",
            "max_passenger",
            "manufacturing_year",
            "registration",
            "created",
            "updated",
        ]
        read_only_fields = [
            "id",
            "created",
            "updated",
        ]
