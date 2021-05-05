from django.db import models
from django.db.models.base import Model

from core.models import NamedModel, TimestampedModel, DescriptionModel


TYPE_CHOICES = [
    ("Internal Combustion", "Internal Combustion"),
    ("Hybrid", "Hybrid"),
    ("Electric", "Electric"),
]


class Category(NamedModel, TimestampedModel, DescriptionModel):
    """
    A model to store categories of a Car.
    """

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"


class Manufacturer(NamedModel, TimestampedModel, DescriptionModel):
    """
    A model to store the details of a Manufacturer.
    """

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return f"{self.name}"


class Car(TimestampedModel):
    """
    A model to store the details of a Car.
    """

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name="Manufacturer",
    )
    model = models.CharField(
        verbose_name="Model of the car",
        max_length=256,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="cars",
        null=True,
        blank=True,
    )
    powertrain = models.CharField(
        verbose_name="Type",
        max_length=256,
        choices=TYPE_CHOICES,
        default="Internal Combustion",
    )
    max_passenger = models.PositiveIntegerField(
        verbose_name="Maximum number of passengers",
    )
    manufacturing_year = models.CharField(
        verbose_name="Year of manufacture",
        max_length=256,
    )
    registration = models.CharField(
        verbose_name="Registration number",
        max_length=256,
    )

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.model}"
