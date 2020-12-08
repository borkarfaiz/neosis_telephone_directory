from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render

from django_tables2 import RequestConfig
from django_tables2 import LazyPaginator

from .filters import ContactsFilter

from .models import Contacts
from .tables import ContactsTable


User = get_user_model()

class ContactListView(LoginRequiredMixin, ListView):
    model = Contacts
    slug_field = "id"
    slug_url_kwarg = "id"

contact_list_view1 = ContactListView.as_view()


# views.py
def contact_list_view2(request):
    contacts = Contacts.objects.filter(user=request.user)
    # contacts = ContactsFilter(request.GET, queryset=contacts)
    table = ContactsTable(contacts)
    RequestConfig(
        request, paginate={'per_page': 20, "paginator_class": LazyPaginator}
    ).configure(table)
    return render(request, "telephone_directory/contacts_list.html", {
        "table": table
    })


from django_tables2 import SingleTableMixin
from django_filters.views import FilterView


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = ContactsTable
    template_name = "telephone_directory/contacts_list.html"
    filterset_class = ContactsFilter

contact_list_view2 = FilteredPersonListView.as_view()