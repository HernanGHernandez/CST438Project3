import django_filters
from .models import Parking


class lotFilter(django_filters.FilterSet):
    class Meta:
        model = Parking
        fields = ['lot']
