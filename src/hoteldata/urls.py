from django.urls import path

from .views import CityHotelListView, HotelListView

urlpatterns = [
    path("", HotelListView.as_view()),
    path("<str:city>/", CityHotelListView.as_view()),
]
