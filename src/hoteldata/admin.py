from django.contrib import admin

from .models import City, Hotel


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("__str__", "hotels")

    def hotels(self, obj):
        """
        Display the number of hotels in the city.
        """
        return obj.get_num_hotels()


admin.site.register(Hotel, admin.ModelAdmin)
