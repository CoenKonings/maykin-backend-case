from django import forms

from .models import City


class CityForm(forms.Form):
    city = forms.ModelMultipleChoiceField(
        queryset=City.objects.exclude(hotel=None),
        label="City",
        to_field_name="abbreviation",
        blank=True,
    )
