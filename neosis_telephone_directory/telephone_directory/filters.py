import django_filters

from .models import Contacts

class ContactsFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    last_name = django_filters.CharFilter(lookup_expr="icontains")
    mobile_number = django_filters.CharFilter(lookup_expr="icontains")
    landline_number = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name']