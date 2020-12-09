from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render, reverse
from django.core.exceptions import  ValidationError

from django_tables2 import RequestConfig
from django_tables2 import LazyPaginator

from .filters import ContactsFilter
from .forms import PictureForm
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
    form_class = PictureForm
    
    def get_success_url(self):
        print('get_success_url')
        return reverse('contacts:contact_list_view')

    def form_valid(self, form):
        print('form_valid')
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        # if self.object.profile_pic:
        #     file_size = self.object.profile_pic._file.size
        #     five_hundred_kb = 1024 * 100
        #     if file_size > five_hundred_kb:
        #         raise ValidationError("Image file too large ( > 500kb )")

        self.object.save()
        return super(ModelFormMixin, self).form_valid(form)

    # def clean_profile_pic(self, form):
    #     print('clean_profile_pic')
    #     image = self.object.get('profile_pic')
    #     if image:
    #         # if image._size > 4*1024*1024:
    #         if image._size > 4:
    #             raise ValidationError("Image file too large ( > 4mb )")
    #         return image

contact_create_view = ContactCreateView.as_view()


