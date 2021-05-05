from django.db import models


class NamedModel(models.Model):
    """
    An abstract base model that provides a mandatory ``name`` field.
    """

    name = models.CharField(
        max_length=100,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class TimestampedModel(models.Model):
    """
    An abstract base model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """

    created = models.DateTimeField(
        verbose_name="Date created",
        auto_now_add=True,
        blank=True,
        db_index=True,
    )
    updated = models.DateTimeField(
        verbose_name="Last updated",
        auto_now=True,
        blank=True,
    )

    class Meta:
        abstract = True


class DescriptionModel(models.Model):
    """
    An abstract base model that provides a ``description`` field.
    """

    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
