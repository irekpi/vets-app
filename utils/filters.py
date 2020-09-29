import django_filters
from users.models import Pet


class PetsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact', label='Imie pupila')
