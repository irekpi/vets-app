import django_filters


class PetsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact', label='Imie pupila')
