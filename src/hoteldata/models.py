from django.db import models


class City(models.Model):
    name = models.CharField(max_length=85)
    # 3 letter identifier. Used to differentiate cities with the same name.
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class Hotel(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    index = models.PositiveSmallIntegerField(
        db_comment="Combines with city abbreviation to create hotel code."
    )
