from django.views.generic import ListView

from .forms import CityForm
from .models import Hotel


class HotelListView(ListView):
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            context["city_form"] = CityForm(self.request.GET)
        else:
            context["city_form"] = CityForm()

        return context

    def get_queryset(self, **kwargs):
        city_form = CityForm(self.request.GET)

        if city_form.is_valid():
            print(city_form.cleaned_data)
            return Hotel.objects.filter(city__in=city_form.cleaned_data["city"]).all()
        else:
            return Hotel.objects.all()
