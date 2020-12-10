
from datetime import date
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import  ValidationError
from django.db.models import Sum
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import ModelFormMixin
from django.shortcuts import render, reverse

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, RequestConfig 

import pandas as pd

from .filters import ContactsFilter
from .forms import PictureForm
from .models import Contacts, ContactViewCount
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

    def get_queryset(self):
        return Contacts.objects.filter(user_id=self.request.user.id)

    def get_labels_data(self):
        today = date.today()
        data_for_days = 7
        data_set = ContactViewCount.objects.filter(
            contact_id=self.kwargs['pk'],
            count_date__gt=today - relativedelta(days=data_for_days),
        ).values("count_date", "count").order_by("count_date")
        total_views = ContactViewCount.objects.filter(
            contact_id=self.kwargs['pk']
        ).aggregate(
            total_views=Sum('count')
        ).get('total_views') or 0
        label_dates = [today - relativedelta(days=i) for i in range(data_for_days-1, -1, -1)]
        date_counts = []
        df = pd.DataFrame(data_set)
        for label_date in label_dates:
            if df.shape[0] == 0:
                date_counts = [0 for i in range(data_for_days)]
                break
            found_data = df[df["count_date"] == label_date]
            try:
                count = found_data.iloc[0]['count']
                print(count)
            except IndexError:
                count = 0
            
            date_counts.append(count)
        label_dates = [str(label_date) for label_date in label_dates]
        data_present = any(date_counts)
        return {
            'labels': label_dates,
            'data': date_counts,
            'data_present': data_present,
            'total_views': total_views,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pie_chart_data = self.get_labels_data()
        context.update(pie_chart_data)
        return context
    

contact_detail_view = ContactsDetailView.as_view()
