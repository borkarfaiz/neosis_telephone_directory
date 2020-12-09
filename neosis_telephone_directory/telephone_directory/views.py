from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render, reverse
from django.core.exceptions import  ValidationError

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, RequestConfig 

from .filters import ContactsFilter
from .forms import PictureForm
from .models import Contacts
from .tables import ContactsTable

from django_tables2 import SingleTableMixin

User = get_user_model()


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
    form_class = PictureForm
    
    def get_success_url(self):
        print('get_success_url')
        return reverse('contacts:contact_list_view')

    def form_valid(self, form):
        print('form_valid')
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

contact_create_view = ContactCreateView.as_view()


class ContactsDetailView(LoginRequiredMixin, DetailView):
    model = Contacts


contact_detail_view = ContactsDetailView.as_view()