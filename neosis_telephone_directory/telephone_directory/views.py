from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render, reverse

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
    template_name = "telephone_directory/contacts_list.html"
    filterset_class = ContactsFilter
    table_class = ContactsTable
    # paginator_class = LazyPaginator
    paginate_by = 20

    def get_table_data(self):
        self.filter = ContactsFilter(
            self.request.GET, 
            queryset=Contacts.objects.filter(user=self.request.user),
            request=self.request
            )
        return self.filter.qs


contact_list_view2 = FilteredPersonListView.as_view()


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contacts
    fields = [
        "first_name", "middle_name", "last_name", "email", "mobile_number", 
        "landline_number",
        ]
    
    def get_success_url(self):
        return reverse('contacts:contact_list_view')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

contact_create_view = ContactCreateView.as_view()
