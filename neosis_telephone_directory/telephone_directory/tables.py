import itertools

import django_tables2 as tables

from .filters import ContactsFilter
from .models import Contacts

class ContactsTable(tables.Table):
    No = tables.Column(empty_values=(), orderable=False)
    mobile_number = tables.Column(orderable=False)
    landline_number = tables.Column(orderable=False)
    created = tables.DateColumn(verbose_name="Added")

    def render_No(self):
        self.row_counter = getattr(self, 'row_counter', itertools.count())
        return next(self.row_counter) + 1


    class Meta:
        model = Contacts
        attrs = {"class": "table table-striped"}
        sequence = [
            'No', "first_name", "middle_name", 'last_name', 'mobile_number', 
            'landline_number', 'created',
        ]
        exclude = ["user", "email", "modified", "id", "profile_pic"]