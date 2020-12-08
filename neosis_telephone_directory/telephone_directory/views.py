from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Contacts

User = get_user_model()

class ContactListView(LoginRequiredMixin, ListView):
    model = Contacts
    slug_field = "id"
    slug_url_kwarg = "id"

contact_list_view = ContactListView.as_view()
