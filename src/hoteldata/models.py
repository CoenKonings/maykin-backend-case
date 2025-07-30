from django.db import models


class City(models.Model):
    name = models.CharField(max_length=85)
    # 3 letter identifier. Used to differentiate cities with the same name.
    abbreviation = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"

    def get_num_hotels(self):
        return self.hotel_set.count()


class Hotel(models.Model):
    name = models.CharField()
    # Hotels without cities can be imported automatically, but not added
    # manually.
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    code = models.CharField(
        db_comment="Combines with city abbreviation to create the hotel identifier."
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["city", "code"], name="hotel identifier"),
        ]

    def __str__(self):
        hotel_identifier = self.city.abbreviation + self.code
        return f"{self.name} in {self.city.name} ({hotel_identifier})"
