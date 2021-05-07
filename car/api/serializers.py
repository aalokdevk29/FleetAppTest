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
            "engine",
            "seating_capacity",
            "year",
            "registration",
            "created",
            "updated",
        ]
        read_only_fields = [
            "id",
            "created",
            "updated",
        ]

    def __init__(self, *args, **kwargs):
        """
        Overriden init to handle the explicit field choice.
        """
        remove_fields = kwargs.pop("remove_fields", None)
        super(BaseCarSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # For multiple fields in a list
            [self.fields.pop(field_name) for field_name in remove_fields]


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "category",
            "engine",
            "seating_capacity",
            "year",
            "registration",
            "created",
            "updated",
        ]
        read_only_fields = [
            "id",
            "created",
            "updated",
        ]


class CarUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Car
        fields = [
            "id",
            "manufacturer",
            "model",
            "category",
            "engine",
            "seating_capacity",
            "year",
            "registration",
            "created",
            "updated",
        ]
        read_only_fields = [
            "created",
            "updated",
        ]


class CarDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
