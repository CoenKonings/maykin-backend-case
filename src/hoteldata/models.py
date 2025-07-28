from django.db import models


class City(models.Model):
    # Longest place name in the world has 85 letters.
    name = models.CharField(max_length=85)
    # 3 letter identifier. Used to differentiate cities with the same name.
    abbreviation = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"
