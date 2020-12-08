from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render

from django_tables2 import RequestConfig
from django_tables2 import LazyPaginator

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
    table = ContactsTable(Contacts.objects.filter(user=request.user))
    RequestConfig(request, paginate={'per_page': 20, "paginator_class": LazyPaginator}).configure(table)
    return render(request, "telephone_directory/contacts_list.html", {
        "table": table
    })